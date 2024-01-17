export default class ClassRoom {
  constructor(maxStudentsSize) {
    this._maxStudentsSize = maxStudentsSize;
  }

  get maxStudentsSize() {
    return this._maxStudentsSize;
  }

  set maxStudentsSize(value) {
    if (typeof value === 'number' && value > 0) {
    this._maxStudentsSize = value;
    } else {
    console.error('Invalid value for maxStudentsSize. Please provide a positive number.');
    }
  }
}
