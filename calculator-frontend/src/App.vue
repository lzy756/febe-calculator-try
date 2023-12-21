<template>
  <div id="app">
    <SimpleCalculator />
  </div>
</template>

<script>
import SimpleCalculator from './components/SimpleCalculator.vue';

export default {
  name: 'App',
  components: {
    SimpleCalculator
  }
};
</script>

<style>
  #app {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f5f5f5;
  }
</style>
