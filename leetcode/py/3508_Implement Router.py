from typing import List
from collections import deque


class Router:

    def __init__(self, memoryLimit: int):
        self.packets = deque(maxlen=memoryLimit)

        self.knownPackets = {}
        self.destinations = {}
        self.countCache = {}
        self.size = 0
        self.limit = memoryLimit

    def getPackageKey(self, source: int, destination: int, timestamp: int) -> str:
        return str(source) + "_" + str(destination) + "_" + str(timestamp)

    def getPackageContents(self, packet: List[int]) -> str:
        source = packet[0]
        destination = packet[1]
        timestamp = packet[2]
        return (source, destination, timestamp)

    def dropPackage(self):
        packet = self.packets.pop()
        source, destination, timestamp = self.getPackageContents(packet)
        key = self.getPackageKey(source, destination, timestamp)
        del self.knownPackets[key]
        self.countCache[destination] = {}
        self.destinations[destination].remove(timestamp)
        self.size -= 1
        return packet

    def addPackage(self, packet):
        self.packets.appendleft(packet)
        source, destination, timestamp = self.getPackageContents(packet)
        key = self.getPackageKey(source, destination, timestamp)
        self.knownPackets[key] = key
        if not destination in self.destinations:
            self.destinations[destination] = []
        self.destinations[destination].append(timestamp)
        self.countCache[destination] = {}
        self.size += 1

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = self.getPackageKey(source, destination, timestamp)
        if key in self.knownPackets:
            return False

        if self.size >= self.limit:
            self.dropPackage()

        packet = [source, destination, timestamp]
        self.addPackage(packet)
        return True

    def forwardPacket(self) -> List[int]:
        # print(self.packets[0])
        if self.size > 0:
            return self.dropPackage()
        else:
            return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        key = str(startTime) + "_" + str(endTime)
        if destination in self.countCache:
            cache = self.countCache[destination]
            if key in cache:
                return cache[key]
        else:
            self.countCache[destination] = {}

        count = 0

        if destination not in self.destinations:
            return count
        packets = self.destinations[destination]
        # print(self.destinations)
        for timestamp in packets:
            if timestamp >= startTime and timestamp <= endTime:
                count += 1

        cache = self.countCache[destination]
        cache[key] = count
        # print(count)
        return count


router = Router(2)
router.addPacket(3, 1, 3)
router.addPacket(1, 2, 3)
router.addPacket(4, 5, 3)
router.getCount(1, 2, 3)

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)

# router = Router(3)
# # Initialize Router with memoryLimit of 3.
# router.addPacket(1, 4, 90)
# # Packet is added. Return True.
# router.addPacket(2, 5, 90)
# # Packet is added. Return True.
# router.addPacket(1, 4, 90)
# # This is a duplicate packet. Return False.
# router.addPacket(3, 5, 95)
# # Packet is added. Return True
# router.addPacket(4, 5, 105)
# # Packet is added, [1, 4, 90] is removed as number of packets exceeds memoryLimit. Return True.
# router.forwardPacket()
# # Return [2, 5, 90] and remove it from router.
# router.addPacket(5, 2, 110)
# # Packet is added. Return True.
# router.getCount(5, 100, 110)
# # The only packet with destination 5 and timestamp in the inclusive range [100, 110] is [4, 5, 105]. Return 1.

# router = Router(3)
# # Initialize Router with memoryLimit of 3.
# router.addPacket(1, 4, 90)
# router.getCount(5, 100, 110)
