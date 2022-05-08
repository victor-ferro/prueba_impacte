<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2> Temperaturas </h2>
                
                <div class="col-md-12">
                    <b-table striped hover :items="temperatures" :fields="fields">
                    </b-table>
                </div>

            </div>

        </div>

    </div>
</template>

<script>

import axios from 'axios';

export default {
    data () {
        return {
            fields:[
                {key: 'current_temp', label: 'Temperatura Actual'},
                {key: 'daily_temp', label: 'Temperatura media'},
            ],
            temperatures: []
        }
    },
    methods: {
        getTemperatures () {
            const path = 'http://localhost:8000/api/v1.0/temperatures/latest'
            axios.get(path).then((response) => {
                this.temperatures = [response.data]
            })
            .catch((error) => {
                console.log(error)
            })
        }
        
    },
    created(){
        this.getTemperatures()
    }
}
</script>

<style lang="css" scoped>
</style>