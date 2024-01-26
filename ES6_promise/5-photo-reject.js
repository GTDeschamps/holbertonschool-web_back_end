export default function uploadPhoto(filemName) {
  return Promise.reject(new Error(`${filemName} cannot be processed`));
}
