<template>
      <!-- About -->
  <section class="section" id="about">
    <!-- Title -->
      <div class="container">
        <div class="columns">
            <div class="column is-one-fifth">
                <h3 class="title is-2">Travels</h3>
            </div>
            <div class="column is-four-fifths">
                <div id="map-wrap" style="height: 500px"
                >
                <client-only>
                <l-map :zoom=2 >
                    <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
                    <!-- <l-marker :lat-lng="[55.9464418,8.1277591]"></l-marker> -->
                    <l-marker v-for="(lx, index) in locations" :key="index" :lat-lng="lx.coords">
                        <l-tooltip :content="lx.name" />
                    </l-marker>
                </l-map>
                </client-only>
                </div>
            </div>
        </div>
        <Divider />
    </div>
  </section>
</template>

<script>
// import L from "leaflet";
import Divider      from '~/components/portfolio/Divider.vue'



export default {
  components: { Divider },
  data() {
    return {
      map: null,
      locations: [
        {'name': 'Indianapolis, IN, USA', 'coords': [39.7683331, -86.1583502]} ,
        {'name': 'Bloomington, IN, USA', 'coords': [39.1670396, -86.5342881]} ,
        {'name': 'Chicago, IL, USA', 'coords': [41.8755616, -87.6244212]} ,
        {'name': 'Pictured Rocks, MI, USA', 'coords': [46.5332835, -86.4882206]} ,
        {'name': 'Louisville, KY, USA', 'coords': [38.2542376, -85.759407]} ,
        {'name': 'Mammoth Cave, KY, USA', 'coords': [37.1861597, -86.0999753]} ,
        {'name': 'Niagra Falls, NY, USA', 'coords': [43.09273865, -79.06097976561753]} ,
        {'name': 'Buffalo, NY, USA', 'coords': [42.8867166, -78.8783922]} ,
        {'name': 'New York City, NY, USA', 'coords': [40.7127281, -74.0060152]} ,
        {'name': 'Boston, MA, USA', 'coords': [42.3554334, -71.060511]} ,
        {'name': 'Montpelier, Vermont, USA', 'coords': [44.2602164, -72.5751208]} ,
        {'name': 'Concord, NH, USA', 'coords': [43.207178, -71.537476]} ,
        {'name': 'Augusta, ME, USA', 'coords': [44.3169922, -69.7734278]} ,
        {'name': 'Philadelphia, PA, USA', 'coords': [39.9527237, -75.1635262]} ,
        {'name': 'Nashville, TN, USA', 'coords': [36.1622767, -86.7742984]} ,
        {'name': 'Memphis, TN, USA', 'coords': [35.1460249, -90.0517638]} ,
        {'name': 'Gatlinburg, TN, USA', 'coords': [35.714259, -83.5101638]} ,
        {'name': 'Cincinnati, OH, USA', 'coords': [39.1014537, -84.5124602]} ,
        {'name': 'Columbus, OH, USA', 'coords': [39.9622601, -83.0007065]} ,
        {'name': 'Atlanta, GA, USA', 'coords': [33.7489924, -84.3902644]} ,
        {'name': 'Savannah, GA, USA', 'coords': [32.0790074, -81.0921335]} ,
        {'name': 'Jacksonville, NC, USA', 'coords': [34.7494749, -77.4208221]} ,
        {'name': 'Washington, DC, USA', 'coords': [38.8950368, -77.0365427]} ,
        {'name': 'Richmond, VA, USA', 'coords': [37.5385087, -77.43428]} ,
        {'name': 'Miami, FL, USA', 'coords': [25.7741728, -80.19362]} ,
        {'name': 'Key West, FL, USA', 'coords': [24.5548262, -81.8020722]} ,
        {'name': 'Birmingham, AL, USA', 'coords': [33.5206824, -86.8024326]} ,
        {'name': 'Jackson, MI, USA', 'coords': [42.2416466, -84.425589]} ,
        {'name': 'Tupelo, MI, USA', 'coords': [34.2576067, -88.7033859]} ,
        {'name': 'Hot Springs, AR, USA', 'coords': [34.5038393, -93.0552437]} ,
        {'name': 'Houston, TX, USA', 'coords': [29.7589382, -95.3676974]} ,
        {'name': 'Oklahoma City, OK, USA', 'coords': [35.4729886, -97.5170536]} ,
        {'name': 'Santa Fe, NW, USA', 'coords': [35.6876096, -105.938456]} ,
        {'name': 'White Sands, NW, USA', 'coords': [32.381369, -106.4789925]} ,
        {'name': 'Phoenix, AZ, USA', 'coords': [33.4484367, -112.074141]} ,
        {'name': 'Sedona, AZ, USA', 'coords': [34.8629426, -111.8137097]} ,
        {'name': 'Tucson, AZ', 'coords': [32.2228765, -110.974847]} ,
        {'name': 'Grand Canyon Village, AZ, USA', 'coords': [36.0545151, -112.14063]} ,
        {'name': 'Las Vegas, NV, USA', 'coords': [36.1672559, -115.148516]} ,
        {'name': 'Boulder, CO, USA', 'coords': [40.0149856, -105.270545]} ,
        {'name': 'Denver, CO, USA', 'coords': [39.7392364, -104.984862]} ,
        {'name': 'Salt Lake City, UT, USA', 'coords': [40.7596198, -111.886797]} ,
        {'name': 'Los Angeles, CA, USA', 'coords': [34.0536909, -118.242766]} ,
        {'name': 'San Francisco, CA, USA', 'coords': [37.7790262, -122.419906]} ,
        {'name': 'Seattle, WA, USA', 'coords': [47.6038321, -122.330062]} ,
        {'name': 'Berlin, Germany', 'coords': [52.5170365, 13.3888599]} ,
        {'name': 'Warsaw, Poland', 'coords': [52.2319581, 21.0067249]} ,
        {'name': 'Moscow, Russia', 'coords': [55.7505412, 37.6174782]} ,
        {'name': 'Bangkok, Thailand', 'coords': [13.7524938, 100.4935089]} ,
        {'name': 'Beijing, China', 'coords': [39.9057136, 116.3912972]} ,
        {'name': 'Tokyo, Japan', 'coords': [35.6840574, 139.7744912]} ,
        {'name': 'Kuala Lumpur, Malaysia', 'coords': [3.1516964, 101.6942371]} ,
        {'name': 'Singapore, Singapore', 'coords': [1.357107, 103.8194992]} ,
        {'name': 'Bali, Indonesia', 'coords': [-8.3304977, 115.0906401]} ,
        {'name': 'Seoul, South Korea', 'coords': [37.5666791, 126.9782914]} ,
        {'name': 'Hanoi, Vietnam', 'coords': [21.0358135, 105.84035]} ,
        {'name': 'Krong Siem Reap, Cambodia', 'coords': [13.35990155, 103.86146090506801]} ,
        {'name': 'Phnom Penh, Cambodia', 'coords': [11.5730391, 104.857807]} ,
        {'name': 'Belize City, Belize', 'coords': [17.5000543, -88.2003115]} ,
        {'name': 'Flores, Guatemala', 'coords': [16.9298524, -89.8914817]} ,
        {'name': 'Guatemala City, Guatemala', 'coords': [14.6424667, -90.5131361]} ,
        {'name': 'Mexico City, Mexico', 'coords': [19.4326296, -99.1331785]} ,
        {'name': 'Bogota, Colombia', 'coords': [4.6529539, -74.0835643]} ,
        {'name': 'La Paz, Bolivia', 'coords': [-16.4955455, -68.1336229]} ,
        {'name': 'Uyuni, Bolivia', 'coords': [-20.4628406, -66.8239072]},
        {'name': 'New Orleans, LA, USA', 'coords': [29.9759983, -90.0782127]} ,
        {'name': 'St. Louis, MO, USA', 'coords': [38.6280278, -90.1910154]} ,
        {'name': 'Wichita, KS, USA', 'coords': [37.6922361, -97.3375448]} ,
        {'name': 'Milwaukee, WI, USA', 'coords': [43.0349931, -87.922497]} ,
        {'name': 'Urbana, IL, USA', 'coords': [40.1117174, -88.207301]} ,
        {'name': 'Pullman, WA, USA', 'coords': [46.7304268, -117.173895]} ,
        {'name': 'Moscow, ID, USA', 'coords': [46.7323875, -117.000165]} ,
        {'name': 'Saint John, U.S Virgin Islands', 'coords': [18.335601349999997, -64.75504062120726]} ,
        {'name': 'Saint Thomas, U.S. Virgin Islands', 'coords': [18.34290815, -64.91889970060265]} ,
        {'name': 'Reykjavík, Iceland', 'coords': [64.145981, -21.9422367]} ,
        {'name': 'Providence, RI, USA', 'coords': [41.8239891, -71.4128343]} ,
        {'name': 'Hartford, CT, USA', 'coords': [41.764582, -72.6908547]} ,
        {'name': 'Montreal, Canada', 'coords': [45.5031824, -73.5698065]} ,
        {'name': 'Toronto, Canada', 'coords': [43.6534817, -79.3839347]} 
      ],
    };
  } //,
//   created() {
//     // Check if this code is running on the client-side
//     this.map = L.map("map").setView([0, 0], 2);

//     L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
//       maxZoom: 19,
//     }).addTo(this.map);

//     this.locations.forEach((location) => {
//       L.marker([location.lat, location.lng])
//         .addTo(this.map)
//         .bindPopup(location.name);
//     });

//     this.isClient = process.client;
//   },

//   mounted() {
//     this.map = L.map("map").setView([0, 0], 2);

//     L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
//       maxZoom: 19,
//     }).addTo(this.map);

//     this.locations.forEach((location) => {
//       L.marker([location.lat, location.lng])
//         .addTo(this.map)
//         .bindPopup(location.name);
//     });
//   },
};
</script>

<style scoped>
#map {
  height: 400px;
  width: 100%;
  position: relative; /* Relative position to allow z-index to work */
  z-index: 999; /* Lower z-index to keep it below the navbar */


}
</style>