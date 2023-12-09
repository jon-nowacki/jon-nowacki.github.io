<template>
      <!-- About -->
  <section class="section" id="about">
    <!-- Title -->
      <div class="container">
        <div class="columns">
            <div class="column is-one-fifth">
                <h3 class="title is-2">About</h3>
            </div>
            <div class="column is-four-fifths">
<p class="has-text-justified">
<strong>Overview: </strong>
My general interests is in converting mathematics and knowledge into something tangible. 
I am often the only developer or on a very small mobile team. As such, I generally need to know many things and wear many hats.
I have had multiple roles including full stack engineer, data engineer, analytical engineer, and data scientist. I often work
with a diverse group of stakeholders where I am responsible for tailoring the expectations of the panel into a deliverable within
scope, budget and time restraints. 


</p>
<br>
<p class="has-text-justified">
<strong>Fun: </strong>
You can often find me on the mat. Since my early teens I have been actively involved in wrestling, judo and jujitsu. I spend a lot of time
doing calisthenics, hiking, and biking. More leisure activities include travel, food, cultural events, museums, modern history, 
national parks and UNESCO sites.

I also really like teaching, mentoring and advising. I like helping people figure out how to break down 
complex problems into simpler, more doable things. 

Also, math is hard and I'm constantly trying to get better at it and incorporate it into my work.
</p>



<br>
<p class="has-text-justified"> 
<strong> Short Bio: </strong> My professional and academic interest began junior year at Indiana University Bloomington when I took biochemistry.
Biochemistry provided me with a conceptual understanding of biology using organic chemistry and thermodynamics.
After completing the biochemistry course, I joined a laboratory as a research assistant.
I was pleased with the work I was doing but did not have the level of enthusiasm needed for a lifelong commitment, 
so I began to branch out into other fields, particularly biophysics.
I stayed a fifth year and crammed through mathematics and physics while going to presentations and 
browsing websites searching for research areas that interested me.

What led me into math and physics was the fact that in biochemistry we talked a lot about experimentally observed protein 
functions and pathways but very little about how and why these macromolecules develop and perform these various functions – that’s 
more of a physics kind of question. I decided I wanted to study how these proteins develop structure and function.
 
So, I searched for different programs that would allow me to develop the needed technical skills. I discovered the Bioinformatics Ph.D. 
program at the University of Michigan. Besides my general interests in proteins, I wanted a career path that touched as many 
computational areas as possible. The lab I joined utilized images, statistics, sequence analysis, text, profiles, physics and 
domain knowledge to understand protein structure, function and dynamics.
</p>

<br>
<p class="has-text-justified">
<strong> Alpha Fold and Career Adjustments: </strong>
Nearing the end of my dissertation, the full capabilities of neural networks started to become apparent. The underlying algorithms were
approachable, but the cost to run them not so much. It still surprises me that the cost of my simulations were approximately a couple dollars were
as Googles Deep Mind was spending 250K to a few million per simulation. Since the takeover, I have been spending time working to diversify my skills, 
and finding approaches to harness the newly generated models and technologies in an affordable manner.
</p>

<br>
<p class="has-text-justified">
<strong > Career Interests: </strong> I would consider myself a lifelong learner. 
My work aspirations generally contain the following themes: learn something new, work on interesting problems,
enjoying the workplace culture and my interaction with team members, and being able to pay my mortgage.
</p>

<br>
<div class="content">
    <h4 class="has-text-centered">Technical/Specialized Interests</h4>
      <div class="columns column-mobile-padding" v-for="i in range(0, 12, 3)" :key="i">
                <div class="column is-one-third content is-normal" style="margin: 0px; padding: 0px;">
                    <ul> <li>{{fields[i]}}</li> </ul>
                </div>
                <div class="column is-one-third content is-normal" style="margin: 0px; padding: 0px;">
                   <ul> <li>{{fields[i+1]}}</li> </ul>
                </div>
                <div class="column is-one-third content is-normal" style="margin: 0px; padding: 0px;">
                   <ul> <li>{{fields[i+2]}}</li> </ul>
                </div>
      </div>
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
      career: [
        'Learn new things', 'Work on interesting problems', 'Enjoy the company of team members', 'Being able to pay my mortgage'
      ],

      fields: [
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
        }
    }
}




</script>

<style scoped>


@media screen and (max-width: 768px) {
  .column-mobile-padding {
    margin-bottom: 30px;
  }
}


</style>