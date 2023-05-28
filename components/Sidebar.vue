<template>
  <aside
    class="bg-gradient-to-r from-slate-950 from-10% via-slate-800 via-85% to-slate-700 to-99% text-white rounded-tr-xl rounded-br-lg h-screen overflow-hidden transition-all duration-500"
    :class="{ 'w-12': !isopen, 'w-1/4': isopen }"
  >
    <div>
      <NuxtLoadingIndicator />
      <button
        @click="toggle_button"
        class="bg-slate-950 text-white"
      >
        <Icon
          name="solar:map-arrow-right-bold-duotone"
          :class="{
            'ml-4 transition-all duration-500': !isopen,
            'rotate-180 ml-80 transition-all duration-500':
              isopen,
          }"
          size="30"
        ></Icon>
      </button>
    </div>
    <dictionary />
  </aside>
</template>

<script setup>
let isopen = ref(true);
function toggle_button() {
  isopen.value = !isopen.value;
}
</script>

<style scoped></style>
