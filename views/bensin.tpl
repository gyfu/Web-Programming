% include("header",title=name)
<h1>{{ name }}</h1>
	% placeDict={}
	% for x in data["results"]:
		% if x["company"] == name:
			%placeDict
			<li>{{ x["name"] }} |95 oktan = {{ x["bensin95"] }} |dísel = {{ x["diesel"] }}</li>
		% end
	% end
% include("map")

