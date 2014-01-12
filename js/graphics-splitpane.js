/* Resizable split pane */
$(function() {
	try {
		$('#resizable-top-panel').resizable({handle: 'all', resize: resizeAttr});
		} catch (ex) {
			alert(ex.message);
		}
});

function resizeAttr(event, ui) {
	var change = ui.size.height -
	 $('#resizable-top-panel').attr('height');
	 $('#resizable-bottom-panel').height($('#resizable-bottom-panel').attr('height') - change);
};
 	