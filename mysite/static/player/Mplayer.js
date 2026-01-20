// За основу взят пьюр плеер, буду адаптировать его
const player = document.querySelector('.player'),
      prevBtn = document.querySelector('.btn-prev'),
      playBtn = document.querySelector('.btn-play'),
      nextBtn = document.querySelector('.btn-next'),
      audio = document.querySelector('.audio'),
      progress_container = document.querySelector('.progress_container'),
      progress =  document.querySelector('.progress'),
      songTitle = document.querySelector('.song'),
      imgSrc = document.querySelector('.img_src'),
      yearSlug = player.dataset.year

      trackItems = document.querySelectorAll('.track-item')



// Названия песен
let songs = []


// Песня по умолчанию
let songIndex = 0;

fetch(`/music/api/tracks/?year=${yearSlug}`)
  .then(response => response.json())
  .then(data => {
    songs = data;
    activateTrackList();

    if (songs.length === 0) {
        songTitle.textContent = 'Нет треков для этого года';
        return;
    }

    songIndex = 0;
    loadSong(songIndex);
  });

// Инициализация
function loadSong(index) {
    const track = songs[index];
    songTitle.textContent = track.title;
    audio.src = track.file;
    audio.load();
    setActiveTrack();

    // Ждём, пока браузер узнает длительность трека
    audio.addEventListener('loadedmetadata', () => {
        // Теперь duration доступен
        console.log('Длительность трека:', audio.duration);
    }, { once: true }); // событие одноразовое
}



// Play
function playSong() {
    player.classList.add('play');
    imgSrc.src = '/static/icons/pause.png'; //'icons/pause.png'
    audio.play();
}

// Pause
function pauseSong() {
    player.classList.remove('play');
    imgSrc.src = '/static/icons/play.png'; // 'icons/play.png'
    audio.pause();
}

playBtn.addEventListener('click', () => {
    const isPlaying = player.classList.contains('play') // проверяет, есть ли класс 'play'
    if (isPlaying) {
    pauseSong(); // если есть — ставим на паузу
    }

    else {
    playSong();  // если нет — начинаем воспроизведение
    }

})

//next song
function nextSong() {
    songIndex++;
    if (songIndex > songs.length -1){
        songIndex = 0
    }

    loadSong(songIndex);
    playSong()
}
nextBtn.addEventListener('click', nextSong)


// Prev song
function prevSong(){
 songIndex--
 if (songIndex < 0) {
    songIndex = songs.length -1
 }
    loadSong(songIndex);
    playSong()

}
prevBtn.addEventListener('click', prevSong)


//Прогресс бар
function updateProgress(e) {
    const {duration, currentTime} = e.srcElement
    const progressPercent = (currentTime / duration) * 100
    progress.style.width = `${progressPercent}%`
}
audio.addEventListener('timeupdate', updateProgress)

// Set progress
function setProgress(e) {
    const width = this.clientWidth
    const clickX = e.offsetX
    const duration = audio.duration


    audio.currentTime = (clickX / width) * duration

}
progress_container.addEventListener('click', setProgress)

// Автопереключение после окончания
audio.addEventListener('ended', nextSong)



function setActiveTrack() {
    trackItems.forEach(item => item.classList.remove('active'));
    if (trackItems[songIndex]) {
        trackItems[songIndex].classList.add('active');
    }
}

function activateTrackList() {
    trackItems.forEach(item => {
        item.addEventListener('click', () => {
            const index = Number(item.dataset.index);
            songIndex = index;
            loadSong(songIndex);
            playSong();
            setActiveTrack();
        });
    });
}
