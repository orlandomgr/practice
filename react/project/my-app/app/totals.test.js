import { calculateTotal } from './totals';

describe('calculateTotal', () => {
  test('applies SAVE20 discount correctly', () => {
    const items = [{ price: 30, quantity: 1 }];
    expect(calculateTotal(items, 'SAVE20')).toBe(10);
  });

  test('prevents negative totals when discount exceeds subtotal', () => {
    const items = [{ price: 15, quantity: 1 }];
    // This test is FAILNG: Expected 0, Received -5
    expect(calculateTotal(items, 'SAVE20')).toBe(0);
  });

  test('handles floating point precision for cents', () => {
    const items = [
      { price: 10.25, quantity: 1 },
      { price: 10.70, quantity: 1 }
    ];
    // This test is FAILING: Expected 20.95, Received 20.949999999999999
    expect(calculateTotal(items)).toBe(20.95);
  });
});