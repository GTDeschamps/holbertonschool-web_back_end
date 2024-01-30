export default function cleanSet(set, startString) {
  const valuesArray = Array.from(set);
  const filteredValues = valuesArray.filter((value) => value.startsWith(startString));
  const cleanValues = filteredValues.map((value) => value.slice(startString.length));
  const resultString = cleanValues.join('-');
  return resultString;
}
