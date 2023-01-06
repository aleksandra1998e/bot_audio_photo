from pydub import AudioSegment


def convert_to_wav(audio):
    # Load the audio file
    audio_segment = AudioSegment.from_file(audio.get_file())

    # Convert the audio to WAV format with a 16kHz sample rate
    wav_audio = audio_segment.export(format="wav", bitrate="16k")

    # Return the WAV audio
    return wav_audio
