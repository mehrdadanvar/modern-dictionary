<template>
    <ClientOnly>
        <div class="autocomplete border border-white rounded-lg w-auto">
            <div class="imput">
                <label for="">Type your Word</label>
                <input type="text" name="" id="" class="border border-blue-100" v-model="input_letter">
            </div>
            <div class="result">
                <p>
                    {{ input_letter }}
                </p>
            </div>
        </div>

    </ClientOnly>
</template>

<script setup>
let input_letter = ref("")

let autocomplete = async () => {
    console.log("autocompleted fired")
    console.log(input_letter)
    let url_to_fetch = `https://www.vocabulary.com/dictionary/autocomplete?search=${input_letter.value}`
    console.log(url_to_fetch)
    let response = await fetch(url_to_fetch);
    console.log(response)

}
watch(input_letter, autocomplete)




</script>

<style  scoped></style>