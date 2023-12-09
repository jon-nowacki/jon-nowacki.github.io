<template>
      <!-- About -->
  <section class="section" id="about">
    <!-- Title -->
      <div class="container">
        <div class="columns">
            <div class="column is-one-fifth">
                <h3 class="title is-2">Math</h3>
            </div>
            <div class="column is-four-fifths">
                <p>Web developer with more than 
                  
                Begginner:

                Feature Extraction, Modeling, etc.

                Usage.

                Advanced.

                Expert  
                <strong>4 years</strong> of well-rounded experience with a degree in the
                field of
                <strong>Computer Science</strong>, extensive knowledge of modern Web techniques and love for <strong>Coffee</strong>.
                Looking for an opportunity to work and upgrade, as well as being involved in an organization that
                believes
                in gaining a competitive edge and giving back to the community.
                </p>
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
          fields: [
              {'title': 'Matrix and Tensor Algebra',     'description':  '' },
              {'title': 'Network Topology and Analysis', 'description':  '' },
              {'title': 'Optimization Under Constraints', 'description': '' },
              {'title': 'Graphy Theory and Quiver Mathematics', 'description':  '' },
              {'title': 'General ML/AI and Algorithms', 'description':  '' },
              {'title': 'Probability, Risk Analysis, and Combinatorics', 'description':  '' },
              {'title': 'Transfer Learning', 'description':  '' },
          ]
      }
  }
  
  }
</script>