let corpos_headers = {
  authority: "corpus.vocabulary.com",
  accept: "application/json",
  "accept-language": "en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7,es;q=0.6",
  origin: "https://www.vocabulary.com",
  referrer: "https://www.vocabulary.com/",
  "sec-ch-ua": '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": '"Linux"',
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-site",
  referrerPolicy: "strict-origin-when-cross-origin",
  "user-agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
};
export default defineEventHandler(async (event) => {
  let query = getQuery(event);
  let word = query.word;
  console.log(word);
  let sentences: string[] = [];
  async function call_corpos() {
    try {
      let url = `https://corpus.vocabulary.com/api/1.0/examples/random.json?maxResults=20&query=${word}&startOffset=0`;
      let response = await fetch(url);
      let data = await response.text();
      let inter = JSON.parse(data);
      let returned_sentences = inter.result.sentences;
      returned_sentences.forEach((element: any) => {
        sentences.push(element.sentence);
      });
      //   console.log(returned_sentences);
    } catch (error) {
      if (error) {
        console.log(error);
      }
    }
  }
  await call_corpos();
  return { data: sentences };
});
