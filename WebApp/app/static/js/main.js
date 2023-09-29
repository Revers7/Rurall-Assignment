$(document).ready(function () {
	const tabValue = localStorage.getItem("selected_div");
	if(tabValue !== '') {
		show(tabValue)
	} 
	if (tabValue==null || tabValue=='employee'){ // default!
		show('employee')
	}
	
	// Navbar toggler fix code
	$('.navbar-toggler').click(function(){
		let nav = $('.navbar-collapse')
		if (nav.is(':visible')){
			nav.removeClass('show')
		} else {
			nav.addClass('show')
		}

	})

	$('.dropdown-toggle').click(function(){
		let menu = $(this).parent().find('.dropdown-menu')
		if (menu.is(':visible')){
			menu.css('display', 'none')
		} else {
			menu.css('display', 'block')
		}
	})


	$('input, select, textarea').on('change', function() {
		$('.btn-login').prop('disabled', false);
	});
});

//-- menu1=report menu2=employee -->
function show(param_div_id) {
	let indicator1 =  document.getElementById('emp_ind');
	let indicator2 =  document.getElementById('rep_ind'); 
	let indicator3 =  document.getElementById('ass_ind'); 
	let nav_report =  document.getElementById('nav-report');
	let nav_employee =  document.getElementById('nav-employee');
	let nav_assign=  document.getElementById('nav-assign');

	localStorage.setItem("selected_div",param_div_id);
	if(param_div_id == 'employee'){
		nav_report.classList.remove("selected");
		nav_assign.classList.remove("selected");
		nav_employee.classList.add("selected");
		indicator1.style.background = "lightgray";
		indicator2.style.background = "#e74110";
		indicator3.style.background = "#e74110";
		document.getElementById('employee').style.display = 'block';
		document.getElementById('emp-add').style.display = 'none';
		document.getElementById('report').style.display = 'none';
		document.getElementById('assign').style.display = 'none';
		document.getElementById('rep-add').style.display = 'none';
	}
	
	if (param_div_id == 'report') {
		nav_report.classList.add("selected");
		nav_employee.classList.remove("selected"); 
		nav_assign.classList.remove("selected"); 
		indicator1.style.background = "#e74110";
		indicator3.style.background = "#e74110";
		indicator2.style.background = "lightgray";
		document.getElementById('report').style.display = 'block';
		document.getElementById('employee').style.display = 'none';
		document.getElementById('assign').style.display = 'none';
		document.getElementById('emp-add').style.display = 'none';
		document.getElementById('rep-add').style.display = 'none';
		document.getElementById('ass-add').style.display = 'none';
	}
	
	if (param_div_id == 'assign') {
		nav_report.classList.remove("selected");
		nav_employee.classList.remove("selected"); 
		nav_assign.classList.add("selected"); 
		indicator1.style.background = "#e74110";
		indicator2.style.background = "#e74110";
		indicator3.style.background = "lightgray";
		document.getElementById('assign').style.display = 'block';
		document.getElementById('report').style.display = 'none';
		document.getElementById('employee').style.display = 'none';
		document.getElementById('emp-add').style.display = 'none';
		document.getElementById('rep-add').style.display = 'none';
		document.getElementById('ass-add').style.display = 'none';
	}
	
	
	if(param_div_id == 'emp-add'){
		document.getElementById('emp-add').style.display = 'block';
		document.getElementById('employee').style.display = 'none';
		document.getElementById('report').style.display = 'none';
		document.getElementById('rep-add').style.display = 'none';
		document.getElementById('ass-add').style.display = 'none';
		console.log('display register emp-add menu')
	}
	
	if(param_div_id == 'rep-add'){
		document.getElementById('rep-add').style.display = 'block';
		document.getElementById('emp-add').style.display = 'none';
		document.getElementById('ass-add').style.display = 'none';
		document.getElementById('employee').style.display = 'none';
		document.getElementById('report').style.display = 'none';
		console.log('display register rep-add menu')
	}
	
		if(param_div_id == 'ass-add'){
		document.getElementById('ass-add').style.display = 'block';
		document.getElementById('rep-add').style.display = 'none';
		document.getElementById('emp-add').style.display = 'none';
		document.getElementById('employee').style.display = 'none';
		document.getElementById('report').style.display = 'none';
		console.log('display register ass-add menu')
	}
};

function onSubmitEmployee() {
	localStorage.setItem("selected_div",'employee');
}

function onSubmitReport() {
	localStorage.setItem("selected_div",'report');
}

function onSubmitAssign() {
	localStorage.setItem("selected_div",'assign');
}