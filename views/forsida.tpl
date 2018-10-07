% include("header",title=name)
<h1>Miðannarverkefni</h1>
<ul>
	% for x in data:
		<li><a href="/company?company={{ x }}">{{ x }}</a></li>
	% end
</ul>
<div class="eldri">
	<h1>Eldri verkefni</h1>
	<ul>
		<li><a href="https://verk-1.herokuapp.com/">Verk1</a></li>
		<li><a href="https://verk-2.herokuapp.com/">Verk2</a></li>
		<li><a href="https://verk-3.herokuapp.com/">Verk3</a></li>
	</ul>
</div>
</html>
