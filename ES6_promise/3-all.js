import { uploadPhoto, createUser } from './utils';

export default async function handleProfileSignup() {
  const photopromise = uploadPhoto();
  const userpromise = createUser();

  Promise.all(photopromise, userpromise)
    .then((value) => {
      console.log(`${value[0].body} ${value[1].firstname} ${value[1].lastname}`);
    })
    .catch(() => {
      console.error('signup system offline');
    });
}
