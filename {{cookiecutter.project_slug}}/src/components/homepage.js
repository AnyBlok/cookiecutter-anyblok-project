import { defineComponent } from 'furetui/src/components/factory';

defineComponent('homepage', {
  template: `
    <div class="container has-text-centered">
      <h1 class="title">Welcome in my own Furet UI</h1>
      <div class="column is-half is-offset-one-quarter">
        <img class="image" v-bind:src="logo" alt="Logo">
      </div>
    </div>
  `,
});
