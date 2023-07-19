from TTS.api import TTS
import os

# Running a multi-speaker and multi-lingual model

# List available 🐸TTS models and choose the first one
model_name = TTS.list_models()[0]
# Init TTS
tts = TTS(model_name)

# Output
OUTPUT_PATH=os.environ["OUTPUT_PATH"]
input_path ="Voices_Origin/Joice Belisário Origin/02.mp3"
output_path ="Voices_Origin/Joice Belisário Origin/"

# tts.tts_to_file("Our area is huge. These people embrace the will, the willpower, that they have the courage to take the first step and not give up. Because for several reasons I already thought about giving up, and I said, how good that I didn't give up. So, to pass on to these people is what? Don't give up. If you have a path to follow, follow it. Study, don't stop studying. Especially within my area, which I talk to my students all the time. Don't stop studying, don't take a course thinking that's enough. The world is vast and we need to explore as much as possible. Be a reference, become better and better as a person, as a professional.", language='en' speaker_wav=input_path, file_path=output_path+"V2_outputEN.wav")


# Run TTS

# ❗ Since this model is multi-speaker and multi-lingual, we must set the target speaker and the language
# Text to speech with a numpy output
# wav = tts.tts("This is a test! This is also a test!!", speaker=tts.speakers[1], language=tts.languages[0])
# Text to speech to a file
# tts.tts_to_file(text="Hello world!", speaker=tts.speakers[0], language=tts.languages[0], file_path="output.mp3")

# Running a single speaker model

# Init TTS with the target model name
# tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=True, gpu=False)

# Run TTS
tts.tts_to_file(text="Ich bin eine Testnachricht.", file_path=OUTPUT_PATH)

# Example voice cloning with YourTTS in English, French and Portuguese
# tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=True, gpu=False)
# tts.tts_to_file("The scenes you just saw are from the realistic nanofilm process. My name is Joyce Belizarro, I'm here to help you and teach you how to make the thinnest and most realistic films you've ever seen. And for you who are already a professional in the field, and want to update yourself, specialize in the field of nanofilm, I can help you. We have a premium mentorship, the vacancies are already open and the course is totally VIP and in-person.", speaker_wav=input_path, language="en", file_path=output_path+"V1_outputEN.wav")
# tts.tts_to_file("Las escenas que acabaron de ver son del procedimiento de nanofilos realistas. Mi nombre es Joyce Belizarro, estoy aquí para ayudarte y enseñarte a hacer los fios más finos y realistas que has visto. Y para ti que ya eres profesional de la área, quieres actualizarte, especializarte dentro de la área de nanofilos, yo puedo ayudarte. Tenemos la mentoría premia, las escenas ya están abiertas y el curso es totalmente VIP y presencial.", speaker_wav=input_path, language="fr-fr", file_path=output_path+"V1_outputFR.wav")
# tts.tts_to_file("Por que preciso retirar minha micropigmentação antiga para fazer uma nanopigmentação? É impossível a gente pegar algo que está escuro, chumbado, acinzentado e projetar ali fios extremamente finos e realistas. Não tem como. No dia do procedimento pode até ficar legal, sim. Porém daqui 30, 40 dias aquela sobrancelha antiga vai sobressair e a nanopigmentação que nós fizemos por cima não vai aparecer. Joyce, e qual a solução? Nós temos remoção a laser, um método seguro, eficaz, que vai remover toda a sua micropigmentação antiga para preparar e receber a nanopigmentação.", speaker_wav=input_path, language="pt-br", file_path=output_path+"outputPT.wav")

tts.tts_to_file("Our area is huge. These people embrace the will, the willpower, that they have the courage to take the first step and not give up. Because for several reasons I already thought about giving up, and I said, how good that I didn't give up. So, to pass on to these people is what? Don't give up. If you have a path to follow, follow it. Study, don't stop studying. Especially within my area, which I talk to my students all the time. Don't stop studying, don't take a course thinking that's enough. The world is vast and we need to explore as much as possible. Be a reference, become better and better as a person, as a professional.", speaker_wav=input_path, language="en", file_path=output_path+"V2_outputEN.wav")
# tts.tts_to_file("nuestra área está inmensa, que estas personas abracen la voluntad, la fuerza de la voluntad, que tengan el ánimo de dar el primer paso y de no desistir, porque por varios motivos ya pensé en desistir y yo dije, qué bueno que no desistí. Entonces, pasar a estas personas es no desistir, si tienes un camino a seguir, sigue, estudia, no pares de estudiar, principalmente dentro de mi área que yo hablo con mis alumnas todo el tiempo, no pares de estudiar, no hagas un curso pensando que aquello allí es suficiente. El mundo es vasto y necesitamos explorar lo máximo posible de aquello, ser referencia, tornar cada vez mejor como persona, como profesional.", speaker_wav=input_path, language="fr-fr", file_path=output_path+"V2_outputFR.wav")
# tts.tts_to_file("Por que preciso retirar minha micropigmentação antiga para fazer uma nanopigmentação? É impossível a gente pegar algo que está escuro, chumbado, acinzentado e projetar ali fios extremamente finos e realistas. Não tem como. No dia do procedimento pode até ficar legal, sim. Porém daqui 30, 40 dias aquela sobrancelha antiga vai sobressair e a nanopigmentação que nós fizemos por cima não vai aparecer. Joyce, e qual a solução? Nós temos remoção a laser, um método seguro, eficaz, que vai remover toda a sua micropigmentação antiga para preparar e receber a nanopigmentação.", speaker_wav=input_path, language="pt-br", file_path=output_path+"outputPT.wav")

# tts.tts_to_file("Why do I need to remove my old micro pigmentation to do a nano pigmentation? It is impossible for us to take something that is dark, mottled, grayish and project extremely thin and realistic threads there. There is no way. On the day of the procedure it can even look cool, yes. However, in 30 to 40 days, that old eyebrow will stand out and the nano pigmentation that we did on top will not appear. Joyce, what is the solution? We have laser removal, a safe, effective method that will remove all your old micro pigmentation to prepare and receive the nano pigmentation.", speaker_wav=input_path, language="en", file_path=output_path+"V3_outputEN.wav")
# tts.tts_to_file("¿Por qué necesito retirar mi micropigmentación antigua? Para hacer una nanopigmentación. Es imposible que nos pongamos algo que está oscuro, chumbado, ascensionado, y proyectar allí hilos extremadamente finos y realistas. No hay manera. En el día del procedimiento puede até quedar bien, sí. Pero, en 30 o 40 días, esa sobrancella antigua va a sobresalir y la nanopigmentación que hicimos por encima no va a aparecer. Joyce, ¿cuál es la solución? Tenemos la remoción a la laser. Un método seguro, eficaz, que va a remover toda su micropigmentación antigua para preparar y recibir la nanopigmentación.", speaker_wav=input_path, language="fr-fr", file_path=output_path+"V3_outputFR.wav")
# tts.tts_to_file("Por que preciso retirar minha micropigmentação antiga para fazer uma nanopigmentação? É impossível a gente pegar algo que está escuro, chumbado, acinzentado e projetar ali fios extremamente finos e realistas. Não tem como. No dia do procedimento pode até ficar legal, sim. Porém daqui 30, 40 dias aquela sobrancelha antiga vai sobressair e a nanopigmentação que nós fizemos por cima não vai aparecer. Joyce, e qual a solução? Nós temos remoção a laser, um método seguro, eficaz, que vai remover toda a sua micropigmentação antiga para preparar e receber a nanopigmentação.", speaker_wav=input_path, language="pt-br", file_path=output_path+"outputPT.wav")


# Example voice conversion converting speaker of the `source_wav` to the speaker of the `target_wav`

tts = TTS(model_name="voice_conversion_models/multilingual/vctk/freevc24", progress_bar=False, gpu=False)
tts.voice_conversion_to_file(source_wav="my/source.mp3", target_wav="my/target.mp3", file_path="output.mp3")

# Example voice cloning by a single speaker TTS model combining with the voice conversion model. This way, you can
# clone voices by using any model in 🐸TTS.

tts = TTS("tts_models/de/thorsten/tacotron2-DDC")
tts.tts_with_vc_to_file(
    "Wie sage ich auf Italienisch, dass ich dich liebe?",
    speaker_wav="target/speaker.mp3",
    file_path="ouptut.mp3"
)

# Example text to speech using [🐸Coqui Studio](https://coqui.ai) models.

# You can use all of your available speakers in the studio.
# [🐸Coqui Studio](https://coqui.ai) API token is required. You can get it from the [account page](https://coqui.ai/account).
# You should set the `COQUI_STUDIO_TOKEN` environment variable to use the API token.

# If you have a valid API token set you will see the studio speakers as separate models in the list.
# The name format is coqui_studio/en/<studio_speaker_name>/coqui_studio
models = TTS().list_models()
# Init TTS with the target studio speaker
tts = TTS(model_name="coqui_studio/en/Torcull Diarmuid/coqui_studio", progress_bar=True, gpu=False)
# Run TTS
tts.tts_to_file(text="This is a test.", file_path=OUTPUT_PATH)
# Run TTS with emotion and speed control
tts.tts_to_file(text="This is a test.", file_path=OUTPUT_PATH, emotion="Happy", speed=1)


#Example text to speech using **Fairseq models in ~1100 languages** 🤯.

#For these models use the following name format: `tts_models/<lang-iso_code>/fairseq/vits`.
#You can find the list of language ISO codes [here](https://dl.fbaipublicfiles.com/mms/tts/all-tts-languages.html) and learn about the Fairseq models [here](https://github.com/facebookresearch/fairseq/tree/main/examples/mms).

# TTS with on the fly voice conversion
api = TTS("tts_models/deu/fairseq/vits")
api.tts_with_vc_to_file(
    "Wie sage ich auf Italienisch, dass ich dich liebe?",
    speaker_wav="target/speaker.mp3",
    file_path="ouptut.mp3"
)