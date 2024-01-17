import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = this.validateNumber(floors, 'floors');
  }

  get floors() {
    return this._floors;
  }

  set floors(value) {
    this._floors = this.validateNumber(value, 'floors');
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors.`;
  }

  validateNumber(value, attribute) {
    if (typeof value !== 'number' || isNaN(value) || value <= 0) {
      throw new Error(`${attribute} must be a valid positive number.`);
    }
    return value;
  }
}
