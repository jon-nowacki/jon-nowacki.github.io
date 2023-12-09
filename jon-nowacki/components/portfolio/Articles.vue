<template>
      <!-- About -->
  <section class="section" id="about">
    <!-- Title -->
      <div class="container">
        <div class="columns">
            <div class="column is-one-fifth">
                <h3 class="title is-2">Articles</h3>
            </div>
            <div class="column is-four-fifths">
                <!-- grants/scholarhships/fellowships -->
                <p>Web developer with more than <strong>4 years</strong> of well-rounded experience with a degree in the
                field of
                <strong>Computer Science</strong>, extensive knowledge of modern Web techniques and love for <strong>Coffee</strong>.
                Looking for an opportunity to work and upgrade, as well as being involved in an organization that
                believes
                in gaining a competitive edge and giving back to the community.
                <!-- Publications and Research Papers -->

                </p>
            </div>
        </div>
    </div>
  </section>
</template>

<script>
import Divider      from '~/components/portfolio/Divider.vue'

export default { 
  components: { Divider },
  data() {
    return {

      papers: [
          'General Data Science and Data Engineering',
          'Matrix and Tensor Algebra',
          'Network Topology and Analysis',
          'Optimization Under Constraints',
          'Graphy Theory and Quiver Mathematics',
          'General ML/AI and Algorithms',
          'Probability, Risk Analysis, and Combinatorics',
          'Transfer Learning',
          'Macromolecular Structure', 'Metabolomics', 'Signal Transduction and Regulation',
          'Image Processing', 'Natural Language Processing', 'Hybrid Cloud', 
          'Novel Projects',
          'Financial/Investment Mathematics' 
      ],
    grants: [

// NIGMS Post Baccalaureate Research Education Program – (2009-2010) 
// Louis Stokes Alliance for Minority Participation – (2007).
// Student Research Opportunities Program – (Summer 2006).
// Involved in Hudson and Holland Scholarship Program, a merit-based scholarship renewable over four years – (2004-2008).
// 

      ]
    }
  }
}


</script>
