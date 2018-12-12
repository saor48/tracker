// name:accepted, average:2.5

var data = jQuery("#data").text();
var ndata = data;
for (var i = 18; i--; ) {
    ndata = ndata.replace("'",'"') ;
}
var jdata = JSON.parse(ndata); 

drawbar(jdata);

function drawbar(data){
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
    
    // bargraph area
    var svgbar = d3.select("#bar").append("svg")
        .attr("width", w)
        .attr("height", h);
    
    // enter data
    var bar1 =  svgbar.selectAll("rect")
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
    var text1 = svgbar.selectAll("text")
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
    var formatDecimal = d3.format(".1f");
    text1.append("text")
        .text(function(d) {
            return formatDecimal(d.average);
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