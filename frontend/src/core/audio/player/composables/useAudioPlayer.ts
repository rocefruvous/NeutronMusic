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

  const seek = (e: Event) => {
    const el = audio.value;
    if (!el) return;
    el.currentTime = +(e.target as HTMLInputElement).value;
  };

  // ── sync playback state + time ──
  watchEffect((onCleanup) => {
    const el = audio.value;
    if (!el) return;

    const onTime = () => (currentTime.value = el.currentTime);
    const onMeta = () => (duration.value = el.duration);
    const onPlay = () => (isPlaying.value = true);
    const onPause = () => (isPlaying.value = false);

    el.addEventListener("timeupdate", onTime);
    el.addEventListener("loadedmetadata", onMeta);
    el.addEventListener("play", onPlay);
    el.addEventListener("pause", onPause);

    onCleanup(() => {
      el.removeEventListener("timeupdate", onTime);
      el.removeEventListener("loadedmetadata", onMeta);
      el.removeEventListener("play", onPlay);
      el.removeEventListener("pause", onPause);
    });
  });

  // ── react to src changes + autoplay ──
  watchEffect((onCleanup) => {
    const el = audio.value;
    const s = src();

    if (!el || !s) return;

    currentTime.value = 0;
    duration.value = 0;

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
