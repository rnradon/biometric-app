var plugins = (function() {
	function showBack() {
      	document.getElementById("back").style.display = "block";
    }
	function init() {
		showBack()
	}
    return {
      init : init
    };
})();