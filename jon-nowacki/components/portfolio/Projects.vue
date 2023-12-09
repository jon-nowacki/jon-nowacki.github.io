<template>
      <!-- Project -->
  <section class="section" id="project">
    <!-- Title -->
      <div class="container">
        <div class="columns">
            <div class="column is-one-fifth">
                <h3 class="title is-2">Projects</h3>
            </div>
            <div class="column is-four-fifths">
                <div v-for="(project, index) in projects" :key="index">
                    <article class="message is-link mb-5">
                    <div class="message-header">
                       <p> 
                       <nuxt-link :to="project.href.name" style="text-decoration:none">{{project.title}}</nuxt-link>
                       </p>
                    </div>
                    <div class="message-body">
                        {{project.description}}

                        <nuxt-link :to="project.href.name"><strong> Click to view full page. </strong> </nuxt-link> 
                    </div>
                    </article>
                </div>
            </div>
        </div>
        <Divider />
    </div>
  </section>
</template>

<script>
import Divider      from '~/components/portfolio/Divider.vue'

export default {
    components: { Divider },
    data() {
        return {
            projects: [
                {'title': 'Macromolecular Modeling: Template Based Assembly of Complex Structures', 'description': macromolecular_description, 'href': {"name":"/projects/macromolecular"} },
                // {'title': 'MDM: Full Stack Master Data Management System', 'description': mdm_description, 'href': {"name":"/projects/mdm"} },
                {'title': 'VuConn: Virtualized User Connections (In Development)', 'description':  vuconn_description, 'href': {"name":"/projects/vuconn"} }
            ]
        }
    }
}

let macromolecular_description = `
I developed one of the first fully automated pipelines for template based quaternary structure prediction 
starting from sequence. The pipeline combines threading templates and domain knowledge from the PDB into a knowledge based energy score. 
The energy score is integrated into a Monte Carlo sampling simulation that drives the initial template closer to the native topology.
`
macromolecular_description = macromolecular_description.replace(/\n/g, ' ')

let mdm_description = `
A full-stack framework for Master Data Management (MDM) is a comprehensive solution that streamlines and centralizes the management of critical organizational data, ensuring data accuracy, consistency, and integrity.
This framework encompasses both front-end and back-end components, offering a holistic approach to MDM.

Efficiency and Automation: Automation of data processes reduces manual errors, accelerates data processing, and improves productivity.
`
mdm_description = mdm_description.replace(/\n/g, ' ')

let vuconn_description = `
The proposed virtual connection is expected to be a critical link that enables an application to interact with a database management system. 
The virtual connections has all the security, reliability, and efficient resource usage of a direct connection while allowing feature extensions generally
not available in data servers. The virtual connections provide improved preformance and capabilities in regards to authentication methods, 
resouce allocation, user management, encryption, and access control mechanisms.
`
vuconn_description = vuconn_description.replace(/\n/g, ' ')



</script>