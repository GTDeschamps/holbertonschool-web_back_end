export default function getFullResponseFromAPI(success) {
  return new Promise((Resolve, reject) => {
    if (success) {
      const result = { status: 200, body: 'Success' };
      Resolve(result);
    } else {
      const error = new Error('The fake API is not working currently');
      reject(error);
    }
  });
}
