import ClassRoom from './0-classroom.js'

export default function initializeRooms(){
  return [new ClassRoom(19), new ClassRoom(28), new ClassRoom(34)];
}
