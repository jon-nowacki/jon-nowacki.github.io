<template>
<!-- Skills -->
<section class="section" id="skills">
<!-- Title -->
<div class="container">
<div class="columns">
    <div class="column is-one-fifth">
        <h3 class="title is-2">Skills</h3>
    </div>

    <div class="column is-four-fith">
        <div class="columns" v-for="i in range(0, 10, 2)" :key="i">
                <div class="column is-half" style="margin-top: 0px; margin-bottom: 0px;">
                        <h4 class ="title is-4" style="margin-bottom: 3px;" > {{ skills[i].category}} </h4>
                        <span class="tag is-link is-medium mr-2 mb-1" v-for="(typex, tx_index) in skills[i].types" :key="tx_index" > {{typex}} </span>
                </div>
                
                <div class="column is-half" style="margin-top: 0px; margin-bottom: 0px">
                        <h4 class ="title is-4" style="margin-bottom: 3px;"> {{ skills[i+1].category}} </h4>
                        <span class="tag is-link is-medium mr-2 mb-1" v-for="(typex, tx_index) in skills[i+1].types" :key="tx_index" > {{typex}} </span>
                </div>
        </div>
    </div>

</div>
<!-- <Divider /> -->
</div>
</section>
</template>

<script>
import Divider      from '~/components/portfolio/Divider.vue'

export default {
    components: { Divider },
    data() {
        return {
            skills: [
                {'category': 'Data Science/ML/AI', 'types': ['Python', 'scikitlearn', 'Pytorch', 'Keras', 'opencv', 'fortran', 'c', 'R' ] },
                {'category': 'Front End', 'types':  ['Vuejs', 'Nuxtjs', 'Bulma', 'Vuetify', 'Javascript', 'CSS', 'SASS/SCSS'] },
                {'category': 'Databases', 'types':  ['Postgresql', 'TSQL', 'SQLITE', 'Redis', 'Neo4j'] },
                {'category': 'Analytics', 'types':  ['Tableau', 'Plotly'] },
                {'category': 'Orchestration, Automation, & ETL/ELT', 'types': ['crontab', 'airflow', 'windows task', 'selenium' ,'dbt', 
                               'SSIS', 'airbyte', 'docker compose'] },
                {'category': 'Middleware', 'types': ['NodeJS', 'Express', 'Nginx', 'API', 'JSON','HTTP Headers', 'YAML', 'XML', 'Postgrest', 'FastAPI', 'HTTP Cookies'] },
                {'category': 'Big Data', 'types':   ['Citus', 'Snowflake', 'Pyspark'] },                
                {'category': 'Deployment', 'types': ['Docker', 'Git', 'pip', 'npm', 'Azure', 'Linode', 'DockerHub'] },
                {'category': 'Administration & Security', 'types':  ['Postgres', 'Linux/Ubuntu', 'OpenSSL', 'OAuth', 'jwt', 'firewall', 'secrets'] },
                {'category': 'Office and Presentation', 'types':  ['Word', 'Illustrator', 'PowerAutomate', 'Excel', 'VBA', 'Latex', 'PowerPoint'] },
                {'category': 'Testing',  'types':   ['Jest', 'CI\\CD', 'unittest'] },
                {'category': 'Business and Soft Skills', 'types':  ['Budgeting', 'Mentoring', 'Advising', 'Project Management', 'Grant Writing'] }
            ]
        }



    },
    methods: {
        range(start, end, step) {
            step = step || 1;
            const result = [];
            for (let i = start; i <= end; i += step) {
            result.push(i);
            }
            return result;
        },
    },


    computed: {
        skills_1() {
            return this.skills.slice(0,6)
        },
        skills_2() {
            return this.skills.slice(6,12)
        }
    }

}
</script>