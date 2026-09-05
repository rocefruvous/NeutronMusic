import { ref, watchEffect } from "vue";

export function useAudioPlayer(src: () => string) {
  const audio = ref<HTMLAudioElement | null>(null);

  const currentTime = ref(0);
  const duration = ref(0);
  const isPlaying = ref(false);

  const togglePlay = async () => {
    const el = audio.value;
    if (!el) return;

    try {
      el.paused ? await el.play() : el.pause();
    } catch {}
  };

  const seek = (time: number) => {
    const el = audio.value;
    if (el) {
      el.currentTime = time;
    }
  };

  watchEffect((onCleanup) => {
    const el = audio.value;
    if (!el) return;

    const updateTime = () => {
      currentTime.value = Number.isFinite(el.currentTime) ? el.currentTime : 0;
    };

    const updateDuration = () => {
      if (Number.isFinite(el.duration)) {
        duration.value = el.duration;
      }
    };

    const onPlay = () => (isPlaying.value = true);
    const onPause = () => (isPlaying.value = false);

    el.addEventListener("timeupdate", updateTime);
    el.addEventListener("loadedmetadata", updateDuration);
    el.addEventListener("loadeddata", updateDuration);
    el.addEventListener("durationchange", updateDuration);
    el.addEventListener("play", onPlay);
    el.addEventListener("pause", onPause);

    onCleanup(() => {
      el.removeEventListener("timeupdate", updateTime);
      el.removeEventListener("loadedmetadata", updateDuration);
      el.removeEventListener("loadeddata", updateDuration);
      el.removeEventListener("durationchange", updateDuration);
      el.removeEventListener("play", onPlay);
      el.removeEventListener("pause", onPause);
    });
  });

  watchEffect((onCleanup) => {
    const el = audio.value;
    const s = src();

    if (!el || !s) return;

    currentTime.value = 0;
    duration.value = 0;

    el.src = s;
    el.load();

    const onCanPlay = async () => {
      el.removeEventListener("canplay", onCanPlay);

      try {
        await el.play();
      } catch {}
    };

    el.addEventListener("canplay", onCanPlay);

    onCleanup(() => {
      el.removeEventListener("canplay", onCanPlay);
    });
  });

  return {
    audio,
    currentTime,
    duration,
    isPlaying,
    togglePlay,
    seek,
  };
}
