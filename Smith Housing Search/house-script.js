// create a variable to store the houses 'database' in
var houses;
// retrieve data from json file
fetch('housedata.json').then(function(response) {
  if(response.ok) {
    response.json().then(function(json) {
      houses = json;
      initialize();
    });
  } else {
    console.log('Network request for houses.json failed with response ' + response.status + ': ' + response.statusText);
  }
});

function initialize() {
  // grab the UI elements that we need to manipulate
  var areas = document.querySelector('#area');
  var accessibility = document.querySelector('#Accessibility');
  var searchTerm = document.querySelector('#searchTerm');
  var searchBtn = document.querySelector('button');
  var main = document.querySelector('main');
  var elevators = document.querySelector('#elevator');
  // keep a record of what the last areas and house entered were
  var lastArea = areas;
  var lastSearch = searchTerm.value;
  var lastAccessibility = Accessibility;
  var lastElevator = elevators;
  // these contain the results of filtering by areas, and search term
  // finalGroup will contain the houses that need to be displayed after
  var areaGroup;
  var finalGroup;
    //Display all houses for the default web
  finalGroup = houses;
  updateDisplay();
    //Display all houses for the default web
  areaGroup = [];
  finalGroup = [];

  // when the search button is clicked, invoke selectCategory()
  // a search running to select the areas of houses we want to display
  searchBtn.onclick = selectArea;

  function selectArea(e) {
    // Use preventDefault() to stop the form submitting
    e.preventDefault();
    //  Clear out the previous search
    areaGroup = [];
    finalGroup = [];
    //If no new reqquest, return previous
    if(areas.value === lastArea && accessibility.value === lastAccessibility && searchTerm.value === lastSearch && lastElevator === elevator.value) {
      return;
    } else {
      // update the record if there are inputs
      lastArea = areas.value;
      lastSearch = searchTerm.value;
	  lastAccessibility = Accessibility.value;
	  lastElevator = elevators.value;
      //if no specidied requests, return all houses
      if(areas.value === 'All' && accessibility.value ==='All' && elevators.value === 'All') {
        areaGroup = houses;
        selectHouses();
      } 
	  else {
          //For comparision, unify word cases.
        var lowerCaseAccessibility = accessibility.value.toLowerCase();
		var lowerCaseElevator = elevators.value.toLowerCase();
        //loop through individual houses in houses
        for(var i = 0; i < houses.length ; i++) {
          // If a house's type property is the same as the chosen areas, we want to update all such houses into areaGroup
          if (areas.value === 'All' && accessibility.value === 'All'){
				areaGroup = houses;
			}
           
		  if(areas.value === 'All' || houses[i].area === areas.value) {
              //filter houses satisifies the requirement of accessability
              if (houses[i].accessible === lowerCaseAccessibility){
				    areaGroup.push(houses[i]);
			  }
			 if (accessibility.value === 'All') {
				if (houses[i].area === areas.value){
						areaGroup.push(houses[i]);
				}
			}
		  }
		  else {
			  if (houses[i].area === areas.value && lowerCaseAccessibility === houses[i].accessible){
					areaGroup.push(houses[i]);
			  }
		  }    
		
		}
        //Move houses out of the list if the elevator attribute does not match the requirement
		if (elevators.value != "All"){
			for(var i = 0; i < areaGroup.length ; i++) {
				console.log(i);
				if (areaGroup[i].elevator != lowerCaseElevator){
					areaGroup.splice(i,1);
                    //Check the previous one
					i-=1;
				}
			}
		}
		// Run selectHouses() after the filtering has been done
		selectHouses();
		}
	}
}
  

  //Futhur filter the houses already filtered by area and other attributes
  function selectHouses() {
      //If no futhur requests, return the areaGroup
    if(searchTerm.value === '') {
      finalGroup = areaGroup;
      updateDisplay();
    } else {
      for(var i = 0; i < areaGroup.length ; i++) {
        if(areaGroup[i].name.indexOf(searchTerm.value) !== -1) {
          finalGroup.push(areaGroup[i]);
        }
      }
      // run updateDisplay() after this second round of filtering has been done
      updateDisplay();
    }

  }

  // start the process of updating the display with the new set of houses
  function updateDisplay() {
    // remove the previous contents of the <main> element
    while (main.firstChild) {
      main.removeChild(main.firstChild);
    }
	

    // if no houses match the search term, display a "No results to display" message
    if(finalGroup.length === 0) {
      var para = document.createElement('p');
      para.textContent = 'No results to display!';
      main.appendChild(para);
    // for each house we want to display, pass its house object to fetchBlob()
    } else {
      for(var i = 0; i < finalGroup.length; i++) {
        fetchBlob(finalGroup[i]);
      }
    }
  }

  // fetchBlob uses fetch to retrieve the image for that house, and then sends the
  // resulting image display URL and house object on to showHouse() to finally
  // display it
  function fetchBlob(house) {
    // construct the URL path to the image file from the house.image property
    var url = 'images/' + house.image;
	//console.log(url);
    // Use fetch to fetch the image, and convert the resulting response to a blob
    // Again, if any errors occur we report them in the console.
    fetch(url).then(function(response) {
      if(response.ok) {
        response.blob().then(function(blob) {
          // Convert the blob to an object URL — this is basically an temporary internal URL
          // that points to an object stored inside the browser
          objectURL = URL.createObjectURL(blob);
          // invoke showHouse
          showHouse(objectURL, house);
        });
		}else {
        console.log('Network request for "' + house.name + '" image failed with response ' + response.status + ': ' + response.statusText);
      }
    });
  }

  // Display a house inside the <main> element
  function showHouse(objectURL, house) {
    // create <section>, <h2>, <p>, and <img> elements
	
    var section = document.createElement('section');
    var heading = document.createElement('h2');
	//var heading2 = document.createElement('h3');
    var para = document.createElement('p');
    var image = document.createElement('img');

    // give the <section> a classname equal to the house "type" property so it will display the correct icon
    //section.setAttribute('class', house.type);

    // Give the <h2> textContent equal to the house "name" property, but with the first character
    // replaced with the uppercase version of the first character
    heading.textContent = house.name+" at "+ house.area;
	var A = "Accessible:No";
	var E = "Elevators:No";
    if(house.accessible==='yes'){
		A = "Accessible:Yes";
	}
	if(house.elevator==='yes'){
		E = "Elevators:yes";
	}
    // 
	para.textContent = "Capacity:"+house.capacity+' '+
        A+' '+E+
        ' '+"Singles:"+house.singles+
        ' '+"Doubles:"+house.doubles+
        ' '+"Triples:"+house.triples+ 
        ' '+"Sharing_bathrooms:"+house.num_sharing_bathrm;
	

    // Set the src of the <img> element to the ObjectURL, and the alt to the house "name" property
    image.src = objectURL;
    image.alt = house.name;

    // append the elements to the DOM as appropriate, to add the house to the UI
    main.appendChild(section);
    section.appendChild(heading);
    section.appendChild(para);
    section.appendChild(image);
  }
}
