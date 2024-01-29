export default function getListStudentsIds(studentsArray) {
  if (!Array.isArray(studentsArray)) {
    return [];
  }
  const idsArray = studentsArray.map((student) => student.id);

  return idsArray;
}
