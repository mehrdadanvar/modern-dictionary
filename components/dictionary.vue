<template>
  <div class="overflow-y-auto px-6">
    <!-- <div class="checked mx-6 my-6 px-6 py-6 border border-slate-300 w-1/4">checked words:{{ checked_words }}</div> -->
    <div class="mx-1 px-1 my-3 flex flex-row h-10">
      <input
        type="text"
        class="text-slate-100 border border-slate-600 px-4 mx-1 rounded-xl bg-slate-800"
        v-model="word"
        @keyup.enter="call_two_apis"
        placeholder="Search"
      />
      <button
        class="bg-slate-800 w-12 rounded-lg border border-slate-600"
        @click="call_two_apis"
      >
        <Icon name="gala:search"></Icon>
      </button>
    </div>
    <div class="response px-4 py-4">
      <div
        v-for="meaning in meanings"
        :key="meaning"
        class="text-slate-400 border border-slate-800 rounded-lg shadow-md shadow-slate-700"
      >
        <div class="">
          <p class="text-slate-50 text-lg">
            Word : {{ meaning.word }}
          </p>
          <p>phonetic : {{ meaning.phonetic }}</p>
          <div class="audio" v-if="meaning.phonetics">
            <audio controls class="">
              <source
                :src="meaning.phonetics[0].audio"
                type="audio/mp3"
              />
            </audio>
          </div>
        </div>
        <div class="meaning-containe pl-8">
          <div
            v-for="x in meaning.meanings"
            :key="x"
            class="rounded-lg pl-4 my-1"
          >
            <p class="pos text-slate-50 text-xl">
              {{ x.partOfSpeech }}
            </p>
            <div v-for="k in x.definitions" :key="k">
              <li class="pl-4">{{ k.definition }}</li>
            </div>
            <div class="ant">
              <div v-if="x.antonyms">exists</div>
              <p v-for="ant in x.antonyms" :key="ant">
                Antonyms : {{ ant }}
              </p>
            </div>
            <div class="syn">
              <span v-for="syn in x.synonyms" :key="syn">
                {{ syn }},
              </span>
            </div>
          </div>
        </div>
      </div>
      <div
        class="rounded-lg px-3 py-2 my-12 border border-slate-800 text-sm shadow-md shadow-slate-700"
        v-show="corpos !== ''"
      >
        <h2 class="text-xl my-2">Synonyms</h2>
        <div class="flex flex-wrap">
          <span
            v-for="x in returned.data"
            :key="x"
            class="bg-slate-700 rounded-md mx-1 px-1 py-1 my-1"
          >
            {{ x }}
          </span>
        </div>
      </div>
      <div class="border border-slate-500 rounded-lg">
        <h2 class="mx-6 my-6 text-xl">Images</h2>
        <div class="flex flex-wrap gap-1">
          <img
            v-for="image in image_urls"
            :key="image"
            :src="image"
            alt=""
            width="100"
          />
        </div>
      </div>
      <div
        class="corps border border-slate-500 rounded-lg my-4 py-4 px-4"
      >
        <h4 class="text-slate-50 text-xl">
          Sample Sentences
        </h4>
        <div class="th-corpos text-slate-400">
          <li
            v-for="s in corpos.data"
            :key="s"
            class="sentence pl-4"
          >
            {{ s }}
          </li>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
//request
let checked_words = ref([]);
let word = ref("");
let meanings = ref("");
let returned = ref("");
console.log(word.value);
let corpos = ref("");
let image_urls = ref([]);
// checked words

// async function load_words() {
//   if (process.client) {
//     checked_words.value = await localStorage.getItem("checked_words");
//   }

// }

// load_words();

async function call_two_apis() {
  if (word.value.length < 1) {
    console.log("not enough words");
  } else {
    // returned.value = "";
    await call_thesauri();
    // await call_dict();
  }
}
async function call_thesauri() {
  //part one inter call thesaurus
  returned.value = "";
  const pre_words = await fetch(
    `http://localhost:3000/api/thesarus?word=${word.value}`
  );
  let words = await pre_words.json();
  console.log(words, "comming from backend");
  returned.value = words;
  // part two external call dictionaryapi
  try {
    const response = await fetch(
      `https://api.dictionaryapi.dev/api/v2/entries/en/${word.value}`
    );
    const info = await response.json();
    console.log(info);
    console.log(typeof info);
    meanings.value = info;
    // word.value = "";
  } catch (error) {
    if (error) {
      console.log(error);
    }
  }
  //part three internal call corpus
  corpos.value = "";
  const corpos_response = await fetch(
    `http://localhost:3000/api/corpos?word=${word.value}`
  );
  console.log(corpos_response);
  const corpos_info = await corpos_response.json();
  console.log(corpos_info);
  corpos.value = corpos_info;
  // part four internal call images
  try {
    let images = await fetch(
      `http://localhost:8000/images/${word.value}`
    );
    let returned_images = await images.json();
    let dict = returned_images.data;
    let final_images = dict[0].message;
    image_urls.value = final_images;
  } catch (error) {
    if (error) {
      console.log(error);
    }
  }
  // part four add the checked word to an array
  checked_words.value.push(word.value);
  localStorage.setItem(
    "checked_words",
    checked_words.value
  );
}
</script>

<style scoped>
audio::-webkit-media-controls-panel {
  background-color: #020617;
}

audio::-webkit-media-controls-mute-button {
  background-color: #64748b;
  border-radius: 50%;
}
</style>
