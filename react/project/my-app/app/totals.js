export const calculateTotal = (items, discountCode) => {
  // Items is an array of objects: { price: number, quantity: number }
  let subtotal = items.reduce((acc, item) => {
    return acc + (item.price * item.quantity);
  }, 0);

  // Apply a flat $20 discount if the code is 'SAVE20'
  if (discountCode === 'SAVE20') {
    subtotal -= 20;
  }

  let finalTotal = subtotal < 0 ? 0 : subtotal

  return Math.round((finalTotal + Number.EPSILON) * 100) / 100;
};
