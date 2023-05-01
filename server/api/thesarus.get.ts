import * as cheerio from "cheerio";
export default defineEventHandler(async (event) => {
  let query = getQuery(event);
  let word = query.word;
  console.log(word);
  let words: string[] = [];
  async function call_thesarus() {
    try {
      let url = `https://www.thesaurus.com/browse/${word}`;
      let response = await fetch(url);
      let html = await response.text();
      const $ = cheerio.load(html);
      let interest = $("div#meanings");
      let listitems = interest.find("li a");
      listitems.each((i, el) => {
        let returned = $(el).text();
        // console.log(returned);
        words.push(returned);
      });
    } catch (error) {
      if (error) {
        console.log(error);
      }
    }
  }
  await call_thesarus();
  return { data: words };
});
