document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('career-test-form');
    const nextButton = document.getElementById('next-btn');
    const resultsDiv = document.getElementById('results');
    const top3List = document.getElementById('top3-list');
    const progressBarFill = document.getElementById('progress-bar');

    // Словарь соответствия букв, профессий и ссылок
    const careerMap = {
        'a': { name: 'Инженер-эколог', link: 'http://127.0.0.1:8000/profession/post_professions/mining_engineer' },
        'b': { name: 'Металлург', link: 'https://technostart25.ru/profession/post_professions/mining_engineer' },
        'c': { name: 'Горный инженер', link: 'https://technostart25.ru/profession/post_professions/mining_engineer' },
        'd': { name: 'Энергетик', link: 'https://technostart25.ru/profession/post_professions/mining_engineer' },
        'e': { name: 'Электротехник', link: 'https://technostart25.ru/profession/post_professions/mining_engineer' },
        'f': { name: 'Инженер-конструктор', link: 'https://technostart25.ru/profession/post_professions/mining_engineer' },
        'g': { name: 'Инженер-проектировщик', link: 'https://technostart25.ru/profession/post_professions/mining_engineer' },
        'h': { name: 'Инженер по автоматизации', link: 'https://technostart25.ru/profession/post_professions/mining_engineer' },
        'i': { name: 'Геодезист', link: 'http://127.0.0.1:8000/profession/post_professions/mining_engineer' }
    };

    // Все вопросы
    const questionElements = document.querySelectorAll('.question');
    const totalQuestions = questionElements.length;
    let currentQuestionIndex = 0;
    let answers = {};

    // Показать первый вопрос
    showQuestion(currentQuestionIndex);

    // Функция для отображения вопроса
    function showQuestion(index) {
        // Скрыть все вопросы
        questionElements.forEach(q => q.classList.remove('active'));

        // Показать текущий вопрос
        if (index >= 0 && index < totalQuestions) {
            const currentQuestionElement = questionElements[index];
            currentQuestionElement.classList.add('active');

            // Обновить кнопку: на последнем вопросе - "Получить результаты", иначе "Следующий"
            if (index === totalQuestions - 1) {
                nextButton.textContent = 'Получить результаты';
            } else {
                nextButton.textContent = 'Следующий вопрос';
            }

            // Сбросить disabled кнопки
            nextButton.disabled = true;

            // Проверить, был ли уже выбран ответ для этого вопроса
            const questionName = `q${index + 1}`;
            const selectedOption = form.querySelector(`input[name="${questionName}"]:checked`);
            if (selectedOption) {
                nextButton.disabled = false;
            }

            // Обновить прогресс
            updateProgress(index + 1);
        }
    }

    // Обновление прогресс-бара
    function updateProgress(current) {
        const percent = (current / totalQuestions) * 100;
        progressBarFill.style.width = `${percent}%`;
    }

    // Обработчик изменения выбора опции
    form.addEventListener('change', function(e) {
        if (e.target.type === 'radio') {
            const questionName = e.target.name;
            answers[questionName] = e.target.value;
            // Разблокировать кнопку, если выбрана опция
            nextButton.disabled = false;
        }
    });

    // Обработчик нажатия на кнопку "Следующий" / "Получить результаты"
    nextButton.addEventListener('click', function () {
        const currentQuestionName = `q${currentQuestionIndex + 1}`;
        const selectedOption = form.querySelector(`input[name="${currentQuestionName}"]:checked`);

        if (!selectedOption) {
            alert('Пожалуйста, выберите ответ.');
            return;
        }

        // Если это последний вопрос, то вычисляем результат
        if (currentQuestionIndex === totalQuestions - 1) {
            calculateAndShowResults();
        } else {
            // Переход к следующему вопросу
            currentQuestionIndex++;
            showQuestion(currentQuestionIndex);
        }
    });

    // Функция для вычисления и отображения результатов
    function calculateAndShowResults() {
        // Подсчёт баллов
        const score = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0};

        for (const answer of Object.values(answers)) {
            if (score.hasOwnProperty(answer)) {
                score[answer]++;
            }
        }

        // Сортировка и получение топ-3
        const sortedScores = Object.entries(score).sort((a, b) => b[1] - a[1]); // Сортировка по убыванию баллов
        const top3Letters = sortedScores.slice(0, 3).map(item => item[0]); // Берём первые 3 буквы

        // Получение названий и ссылок профессий
        const top3Careers = top3Letters.map(letter => careerMap[letter]).filter(item => item); // Убираем undefined, если вдруг

        // Очищаем предыдущие результаты
        top3List.innerHTML = '';

        if (top3Careers.length > 0) {
            top3Careers.forEach(career => {
                const li = document.createElement('li');
                // Создаём ссылку
                const link = document.createElement('a');
                link.href = career.link;
                link.textContent = career.name; // Надпись профессии
                link.target = '_blank'; // Открывать в новой вкладке (по желанию)
                // Стили, чтобы ссылка выглядела как обычная ссылка
                link.style.textDecoration = 'none';
                link.style.color = '#667eea';

                // Добавляем ссылку внутрь <li>
                li.appendChild(link);
                top3List.appendChild(li);
            });
        } else {
            const li = document.createElement('li');
            li.textContent = 'Не удалось определить подходящие профессии.';
            top3List.appendChild(li);
        }

        // Скрываем форму и показываем результаты с анимацией
        form.style.display = 'none';
        resultsDiv.style.display = 'block';
        resultsDiv.style.opacity = '0';
        resultsDiv.style.transform = 'translateY(20px)';
        // Небольшая задержка для запуска анимации
        setTimeout(() => {
            resultsDiv.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            resultsDiv.style.opacity = '1';
            resultsDiv.style.transform = 'translateY(0)';
        }, 10);
    }
});