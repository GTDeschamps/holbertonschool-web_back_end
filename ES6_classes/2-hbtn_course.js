export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this.validateString(name, 'name');
    this._length = this.validateNumber(length, 'length');
    this._students = this.validateArray(students, 'students');
  }

  get name() {
    return this._name;
  }

  set name(value) {
    this._name = this.validateString(value, 'name');
  }

  get length() {
    return this._length;
  }

  set length(value) {
    this._length = this.validateNumber(value, 'length');
  }

  get students() {
    return this._students;
  }

  set students(value) {
    this._students = this.validateArray(value, 'students');
  }

  validateString(value, attribute) {
    if (typeof value !== 'string') {
      throw new Error(`${attribute} must be a string.`);
    }
    return value;
  }

  validateNumber(value, attribute) {
    if (typeof value !== 'number' || isNaN(value)) {
      throw new Error(`${attribute} must be a valid number.`);
    }
    return value;
  }

  validateArray(value, attribute) {
    if (!Array.isArray(value)) {
      throw new Error(`${attribute} must be an array.`);
    }
    return value;
  }
}
