export default class Airport {
  constructor(name, code) {
    if (typeof name !== `string`){
      this._name = this.validateString(name, 'name');
      this._code = this.validateString(code, 'code');
    }
  }

  get name() {
    return this._name;
  }

  set name(value) {
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(value) {
    this._code = code;
  }

  toString() {
    return this._code;
  }
}
