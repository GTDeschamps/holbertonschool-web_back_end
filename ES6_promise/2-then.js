export function handleResponseFromAPI(promise) {
  return new promise((resolve, reject) => {
    promise
    .then(() => {
      console.log('Got a response from the API');
      const result = { status: 200, body: 'success' };
      resolve (result);
    })
    .catch((error) => {
      console.error('Got an error from the API:', error.message);
      reject (new Error(''));
    });
  });
}
