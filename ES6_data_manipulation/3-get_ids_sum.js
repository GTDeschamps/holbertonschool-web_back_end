export default function getSTudentIDsSum(studentsArray) {
  const sum = studentsArray.reduce((total, student) => total + Number(student.id), 0);
  return sum;
}
