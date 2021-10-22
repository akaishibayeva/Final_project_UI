var questions = [];

$(document).ready(function() {

	if (window.location.pathname.includes('/quiz')) {
		// Initialization
		var currentQuestion = 1;

		localStorage.setItem('answers', '');
		localStorage.setItem('questions', '');

		$.ajax({
			url: '/quiz-data',
			method: 'POST',
			data: {},
			success: function(response) {
				questions = response.questions;
				displayQuestions(questions);
			},
			error: function(error) {
				console.log(error);
			}
		});

		function displayQuestions(questions) {
			for (var i = 0; i < questions.length; i++) {
				var question = '<div><h2 class="question-title">\
				'+ questions[i].title +'</h2>\
				<p class="question-error"></p>\
				<div class="question-wrapper">';

				for (var j = 0; j < questions[i].options.length; j++) {
					var option = 
					'<div class="question-input-wrapper">\
						<input class="question-option" type="radio" name="q'+
						(i+1)+'" value="'+questions[i].options[j].value+'">\
						<label class="question-option-title">\
							'+questions[i].options[j].value+'\
						</label>\
					</div>';
					question += option;
				}
				question += '</div></div>';
				$('.q'+(i+1)).append(question);
			}
		}

		$('.quiz-status__number').html(currentQuestion);

		// Next click
		$('.quiz-control__next').click(function() {

			// Validation
			var data = $('.q'+currentQuestion).find('input:checked').val();
			
			if (!data) {
				$('.q'+currentQuestion).find('.question-error').html("Choose one option");
				return false;
			}

			$('.question-error').html('');

			currentQuestion++;

			$('.quiz-status__number').html(currentQuestion);

			$('.question').hide();
			$('.q' + currentQuestion).show();

			if (currentQuestion == 2) {
				$('.quiz-control__back').show();
			}

			if (currentQuestion == 10) {
				$('.quiz-form__button-wrapper').show();
				$('.quiz-control__next').hide();
			}

		});


		// Back click
		$('.quiz-control__back').click(function() {

			currentQuestion--;

			$('.quiz-status__number').html(currentQuestion);

			$('.question').hide();
			$('.q' + currentQuestion).show();

			$('.quiz-form__button-wrapper').hide();

			if (currentQuestion == 1) {
				$('.quiz-control__back').hide();
			}

			if (currentQuestion < 10) {
				$('.quiz-control__next').show();
			}

		});

		// Submit
		$('.quiz-form').submit(function(event) {
			event.preventDefault();
			return false;
		});

		$('.quiz-form__button').click(function() {

			var answers = {};

			for (var i = 1; i <= 10; i++) {
				var option = $('.q'+i).find('input:checked').val();
				if (!option) {
					return false;
				}
				answers['q'+i] = option;
			}

			localStorage.setItem('answers', JSON.stringify(answers));
			localStorage.setItem('questions', JSON.stringify(questions));

			window.location.replace('/result'); 

		});

	} else if (window.location.pathname.includes('/result')) {

		var answers = JSON.parse(localStorage.getItem('answers'));
		questions = JSON.parse(localStorage.getItem('questions'));
		
		var correctCount = 0;

		for (var i = 0; i < questions.length; i++) {
			var question = questions[i];

			var element = '<div class="question">\
				<h2 class="question-title">' + (i+1) + ") " + question.title + '</h2>\
				<div class="question-wrapper">';

			for (var j = 0; j < question.options.length; j++) {
				var option;
				if (question.options[j].value == answers['q'+(i+1)]) {
					if (question.options[j]['is_correct'] == true) {
						correctCount++;
						option = '<div class="question-input-wrapper">\
						<input class="question-option" checked type="radio" value="">\
						<label class="question-option-title question-correct">\
							'+ question.options[j].value +'\
						</label>\
						</div>';
						element += option;
						continue;
					} else {
						option = '<div class="question-input-wrapper">\
						<input class="question-option" checked type="radio" value="">\
						<label class="question-option-title question-fail">\
							'+ question.options[j].value +'\
						</label>\
						</div>';
						element += option;
						continue;

					}
				}

				if (question.options[j]['is_correct'] == true) {
					option = '<div class="question-input-wrapper">\
						<input class="question-option" type="radio" value="">\
						<label class="question-option-title question-correct">\
							'+ question.options[j].value +'\
						</label>\
					</div>';
					element += option;
					continue;
				}

				option = '<div class="question-input-wrapper">\
						<input class="question-option" type="radio" value="">\
						<label class="question-option-title">\
							'+ question.options[j].value +'\
						</label>\
					</div>';

				element += option;
			}

			element += '</div></div>';

			$('.results').append(element);

		}

		$('.quiz-result').html(correctCount);

	}


});