<!DOCTYPE html>
<html>
	<header>
		<meta charset="UTF-16">
		<title>Verkefni 3 - Fréttir</title>
		<link rel="stylesheet" href="./static/stylesheet.css">
	</header>
	<body>
		<div class="banner">
		% include('header.tpl')
		</div>
		<div class="frettir">
			<h1>{{ title }}</h1>
			<img src="/static/mynd{{ myndid }}.jpg"alt="pictureLoadingFailure"width="256px"height="256px">
			<p>{{  body }}</p>
			<h3>{{ author }}</h3>
			<a href="/B">Heim</a>
		</div>
		<div class="fotur">
		% include('footer.tpl')
		</div>
	</body>
</html>
