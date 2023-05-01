export default defineEventHandler(async (event) => {
  let query = getQuery(event);
  let word = query.word;
  console.log(word);
  let words: string[] = [];
  async function call_images() {
    try {
      let url = `http://localhost:8000/images/${word}`;
      let response = await fetch(url);
      let images = await response.json();
      console.log(images.length);
      words.push(images);
    } catch (error) {
      if (error) {
        console.log(error);
      }
    }
  }
  await call_images();
  return { data: words };
});
