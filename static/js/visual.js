// name:accepted, average:2.5

var av = jQuery("#average").text();
for (var i = 18; i--; ) {
    av = av.replace("'",'"');
}
var jav = JSON.parse(av); 
drawbar1(jav);      //average delays

var pos = jQuery("#position").text();
for (var i = 24; i--; ) {
    pos = pos.replace("'",'"');
}
var jpos = JSON.parse(pos);
drawbar2(jpos);      //status position

// average delays
function drawbar1(data){
    //extract values for graph 
    var views = [], rviews = [];
    for (var i = 0; i < data.length; i++) {
        views.push(data[i]['average']);
    }
    
    var w = 600, wname = 300, h = 200;
    var barPadding = 1;
    var setLength = views.length;
    var rowHeight = 30;
    var highest = Math.max.apply(this,views);
    var ratio = (w-wname)/highest;
    for (var i = 0; i < setLength; i++) {
        rviews[i] = parseInt(ratio * views[i]);
    }
    var formatDecimal = d3.format(".1f");
    
    // bargraph1 area
    var svgbar1 = d3.select("#bar1").append("svg")
        .attr("width", w)
        .attr("height", h);
    
    // enter data
    var bar1 =  svgbar1.selectAll("rect")
        .data(rviews)                       
        .enter();
    
    // draw each value    
    bar1.append("rect")
        .attr("y", function(d, i) {
            return i * rowHeight ;
        })
        .attr("x", function(d, i) {
            return w -wname - rviews[i];
        })
        .attr("height", rowHeight - barPadding)
        .attr("width", function(d) {
            return d;
        })
        .attr("fill", "green");
       
    // show names for each bar
    //enter data
    var text1 = svgbar1.selectAll("text")
        .data(data)
        .enter();
    //select key and draw   
    text1.append("text")
        .text(function(d) {
            return d.name;
        })
        .attr("text-anchor", "left")
        .attr("y", function(d, i) {
            return i * rowHeight + (rowHeight) / 2;
        })
        .attr("x",  w - wname + 20)
        .attr("font-family", "sans-serif")
        .attr("font-size", "14px")
        .attr("fill", "blue");
    
    // show days for each bar
    //select key and draw 
    text1.append("text")
        .text(function(d) {
            return formatDecimal(d.average);
        })
        .attr("text-anchor", "left")
        .attr("y", function(d, i) {
            return i * rowHeight + (rowHeight) / 2;
        })
        .attr("x", function(d) {
            return w - wname - 25;
        })
        .attr("font-family", "sans-serif")
        .attr("font-size", "13px")
        .attr("fill", "white");
}

// status position 
function drawbar2(data){
    //extract values for graph 
    var num = [], rnum = [];
    for (var i = 0; i < data.length; i++) {
        num.push(data[i]['number']);
    }
    
    var w = 600, wname = 300, h = 200;
    var barPadding = 1;
    var setLength = num.length;
    var rowHeight = 30;
    var highest = Math.max.apply(this, num);
    var ratio = (w-wname)/highest;
    for (var i = 0; i < setLength; i++) {
        rnum[i] = parseInt(ratio * num[i]);
    }
// bargraph2 area
    var svgbar2 = d3.select("#bar2").append("svg")
        .attr("width", w)
        .attr("height", h);
    
    // enter data
    var bar2 =  svgbar2.selectAll("rect")
        .data(rnum)                       
        .enter();
    
    // draw each value    
    bar2.append("rect")
        .attr("y", function(d, i) {
            return i * rowHeight ;
        })
        .attr("x", function(d, i) {
            return w -wname - rnum[i];
        })
        .attr("height", rowHeight - barPadding)
        .attr("width", function(d) {
            return d;
        })
        .attr("fill", "green");
        
    // show names for each bar
    //enter data
    var text2 = svgbar2.selectAll("text")
        .data(data)
        .enter();
    //select key and draw   
    text2.append("text")
        .text(function(d) {
            return d.name;
        })
        .attr("text-anchor", "left")
        .attr("y", function(d, i) {
            return i * rowHeight + (rowHeight) / 2;
        })
        .attr("x",  w - wname + 20)
        .attr("font-family", "sans-serif")
        .attr("font-size", "14px")
        .attr("fill", "blue"); 
        
    // show number for each bar
    //select key and draw 
    text2.append("text")
        .text(function(d) {
            return d.number;
        })
        .attr("text-anchor", "left")
        .attr("y", function(d, i) {
            return i * rowHeight + (rowHeight) / 2;
        })
        .attr("x", function(d) {
            return w - wname - 20;
        })
        .attr("font-family", "sans-serif")
        .attr("font-size", "13px")
        .attr("fill", "white");
        
}       
