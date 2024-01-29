export default function getStudentsByLocation(studentsArray, city) {
  const filteredStudents = studentsArray.filter((student) => student.location === city);
  return filteredStudents;
}
