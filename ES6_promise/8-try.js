export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw new Error(`Cannot divided by 0`);
  }
  return numerator / denominator;
}
