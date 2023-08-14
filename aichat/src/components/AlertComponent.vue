<template>
    <div class="alert" :class="alertType">
      {{ message }}
    </div>
</template>

<script>
export default {
    props: {
        type: String, // Type of alert (success, error, etc.)
        message: String, // Message to display in the alert
    },

    computed: {
        alertType() {
            return this.type === 'success' ? 'alert-success' : 'alert-error';
        }
    }
};



</script>

<style scoped>
    .alert {
        padding: 10px;
        border-radius: 4px;
        margin-bottom: 10px;
    }

    .alert-success {
    background-color: #dff0d8;
    color: #3c763d;
    }

    .alert-error {
    background-color: #f2dede;
    color: #a94442;
    }
</style>