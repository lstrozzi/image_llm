from openai import OpenAI
import base64

MODEL="meta-llama/Llama-3.2-11B-Vision-Instruct"
IMAGE_PATH="/mnt/d/repos/thalabus/AIServerWeb/wwwroot/images/test/Istruzioni_lavastoviglie2.png"
IMAGE_EXTRACTED_TEXT="""
PRIMO UTILIZZO 
SALE, BRILLANTANTE E DETERSIVO
 SUGGERIMENTO PER IL PRIMO UTILIZZO
 Dopo aver completato l'installazione, togliere i fermi dai cestelli e gli 
elementi elastici di ritegno dal cestello superiore.
 RIFORNIMENTO DEL SERBATOIO DEL SALE
 L'uso di sale previene la formazione di CALCARE sulla superficie dei 
piatti e sui componenti della macchina.
 • È indispensabile che IL SERBATOIO DEL SALE SIA SEMPRE RI
FORNITO.
 • È essenziale quindi che il livello di durezza dell'acqua sia stato impostato.
 Il serbatoio del sale è situato nella parte inferiore della lavastoviglie 
(vedere DESCRIZIONE PRODOTTO) e deve obbligatoriamente essere ri
RIEMPIMENTO DEL DISTRIBUTORE BRILLANTANTE
 L'utilizzo di brillantante facilita il processo di ASCIUGATURA delle stovi
glie. La vaschetta del brillantante A dovrebbe essere riempita quando 
l'indicatore ottico scuro posto sullo sportellino C diventa trasparente.
 C
 fornito ogni volta che la spia dell' indicatore di RIEMPIMENTO SALE 
posta sul pannello comandi è illuminata.
 1. Togliere il cestello inferiore e svitare il tappo 
del serbatoio (ruotare in senso antiorario).
 2. Solo la prima volta: riempire d'acqua il  
serbatoio del sale.
 3. Sistemare opportunamente l'imbuto (vede
re figura) e rifornire il serbatoio del sale fino 
all'orlo (circa 1 kg); Non è inconsueto che 
l'acqua trabocchi leggermente.
 4. Togliere l'imbuto ed eliminare qualsiasi resi
duo di sale dall'areacircostante l'apertura.
 Accertarsi che il tappo sia adeguatamente serrato per evitare l'ingresso 
di detersivo all'interno della vaschetta durante il programma di lavag
gio (ciò potrebbe causare il danneggiamento del dispositivo addol
cente senza possibilità di riparazione).
 1. Aprire il distributore B esercitando opportuna pressione e quindi sollevan
do la linguetta posta sul coperchio.
 2. Versare delicatamente il brillantante fino al segno che indica il li
vello di riferimento massimo (110 ml), ma evitandone la fuoriuscita. 
Nel caso in cui ciò si verifichi, asciugare immediatamente il liquido 
fuoriuscito mediante un panno asciutto.
 3. Abbassare il coperchio fino ad avvertire lo scatto che ne segnala la chiusura.
 Non versare MAI il brillantante direttamente all'interno della 
vaschetta.
 REGOLAZIONE DEL DOSAGGIO DI BRILLANTANTE
 Se non si è completamente soddisfatti del processo di asciugatura, è 
possibile regolare la quantità di brillantante da utilizzare.
 • Azionare la lavastoviglie agendo sul tasto  
Ogni volta che è necessario aggiungere sale, è obbligatorio ese
guire la procedura prima dell'inizio del ciclo di lavaggio  per evita
re rischi di corrosione.
 IMPOSTAZIONE DELLA DUREZZA DELL'ACQUA
 Per consentire che il dispositivo addolcente dell'acqua agisca al meglio, 
è essenziale che l'impostazione del livello di durezza dell'acqua tenga 
conto della sua durezza effettiva nell'utenza domestica. È possibile ot
tenere il valore di durezza dell'acqua nell'utenza domestica rivolgendosi 
al proprio fornitore.
 Il valore predefinito per la durezza dell'acqua viene impostato in fabbrica.
 • Azionare l'apparecchio agendo sul tasto ACCENSIONE/SPEGNIMENTO.
 • Disattivare l'apparecchio agendo sullo stesso tasto ACCENSIONE/SPE
GNIMENTO.
 • Tenere premuto il tasto AVVIO/PAUSA per 5 secondi.
 • Azionare l'apparecchio agendo sul tasto ACCENSIONE/SPEGNIMENTO.
 • Il livello impostato è indicato dal numero di lampeggi del LED  
ACCENSIONE/SPEGNIMENTO. 
• Impostare il livello di durezza dell'acqua desiderato usando la manopola 
di SELEZIONE PROGRAMMI (vedere la TABELLA DI DUREZZA DELL'ACQUA).
 Tabella di durezza dell'acqua
 °dH 
°fH 
Livello
 1
 Gradi  
tedeschi
 Gradi 
francesi
 Dolce 0 - 6 0 - 10
 2 Moderatamente dolce 7 - 11
 °Clark  
Gradi 
inglesi
 0 - 7
 3
 11 - 20
 Medio 12 - 16 21 - 29
 4
 8 - 14
 15 - 20
 Dura 17 - 34 30 - 60 21 - 42
 5
 Molto dura
 35 - 50
 61 - 90
 43 - 62
 • Disattivare l'apparecchio agendo sullo stesso tasto ACCENSIONE/SPE
GNIMENTO.
 La procedura di impostazione è stata completata!
 Non appena completata tale procedura, avviare uno dei programmi senza carico.
 Utilizzare soltanto sale di tipo specifico per lavastoviglie.
 Dopo aver versato il sale all'interno della macchina, la spia riempimento 
SALE si spegne.
 La mancanza di sale nel serbatoio potrebbe danneggiare l'addol
citore d'acqua e la resistenza per effetto dell'accumulo di calcare.
 L'uso del sale è consigliato con qualsiasi tipo di detersivo per lavastoviglie.
 ACCENSIONE/SPEGNIMENTO.
 • Disattivare la lavastoviglie utilizzando lo stesso tasto  
ACCENSIONE/SPEGNIMENTO.
 • Premere tre volte il tasto AVVIO/PAUSA.
 • Azionare la lavastoviglie mediante il tasto  
ACCENSIONE/SPEGNIMENTO.
 • Il livello impostato è indicato dal numero di lampeggi del LED  
AVVIO/PAUSA.
 • Impostare la dose di brillantante da erogare usando la manopola di 
SELEZIONE PROGRAMMI (vedere la TABELLA PROGRAMMI) 
• Disattivare utilizzando il tasto ACCENSIONE/SPEGNIMENTO
 La procedura di impostazione è stata completata!
 Nel caso in cui il livello di brillantante sia impostato su 1 (programma 
ECO), il brillantante non viene erogato. 
A seconda del modello di lavastoviglie è possibile impostare al massimo  
5 livelli di dosaggio. Le impostazioni di fabbrica dipendono dal modello; 
seguire le istruzioni precedenti in base alle caratteristiche del proprio 
apparecchio. 
• In presenza di strisce con sfumature blu sulla superficie dei piatti, 
impostare un livello di dosaggio basso (2-3).
 • In presenza di gocce d'acqua o di calcare sulla superficie dei piatti 
impostare invece dosaggi alti (4-5).
 RIEMPIMENTO DEL DISTRIBUTORE DETERSIVO
 Per aprire il distributore detersivo utilizzare il dispositivo di apertu
ra D. Versare il detersivo esclusivamente nel distributore E asciutta. 
Mettere la dose di detersivo per il prelavaggio direttamente all'in
terno del distributore.
 D 
E
 1. Per il dosaggio corretto del detersivo 
fare riferimento ai dati sopra riporta
ti. La vaschetta E contiene indicatori 
di livello per facilitare il dosaggio del 
detersivo.
 2. 
Eliminare eventuali residui di 
detersivo dai bordi del distributore e 
chiudere il coperchio fino ad avvertire 
lo scatto caratteristico.
 3. 
Chiudere il coperchio del distri
butore sollevandolo fino a portare il 
dispositivo di chiusura in sede.
 Il distributore del detersivo si apre automaticamente quando previsto 
dal programma in uso. 
L'uso di un detersivo non specifico per lavastoviglie potrebbe cau
sare malfunzionamenti o danni all'apparecchio
"""
BASE_URL="https://hedmlqljn2exux-3000.proxy.runpod.net/v1"

client = OpenAI(base_url=BASE_URL, api_key="dummy")
# model_list = client.models.list()
# print(model_list)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
base64_image = encode_image(IMAGE_PATH)

def call_model():
    messages = [
            {"role": "system", "content": """You are a helpful assistant that responds in Markdown. Help me with my math homework!
There are two functions available to you:
- ADD(a,b) - returns the sum of a and b
- MUL(a,b) - returns the product of a and b
In order to use these functions, you have simply to output them in the chat, followed by the two numbers you want to use. For example, if you want to add 3 and 5, you would type ADD(3,5).
You can combine the functions to resolve any expressions you want. For example, if you want to calculate 3+(2*2), you would type ADD(3,MUL(2,2)).

Answer the user's question exclusively using the ADD and MUL functions. Do not output any other text.

Example: 
User: Calculate 3+5+7*3
Assistant: ADD(ADD(3,5),MUL(7,3))
"""},
            {"role": "user", "content": "Calculate 24-3*2+5"}
        ]
    print("Sending question to the LLM...")
    response = client.chat.completions.create(
        messages=messages,
        model=MODEL
    )
    print("...complete.")

    print(response.choices[0].message.content)

def call_model_for_image1():
    print("Sending image to the LLM...")
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user", "content": [
                    {"type": "text", "text": "Qui di seguito trovi un estratto del testo dall'immagine. Puoi usare questo estratto per rispondere alle domande dell'utente."},
                    {"type": "text", "text": IMAGE_EXTRACTED_TEXT}
                ]
            },
            {
                "role": "user", "content": [
                    {"type": "text", "text": """Compila una tabella in markdown sulla durezza dell'acqua, copiando i dati dalla figura"""},
                    {"type": "image_url", "image_url": { "url": f"data:image/png;base64,{base64_image}" } }
                ]
            }
        ],
        temperature=0.1,
        model=MODEL
    )
    print("...complete.")

    print(response.choices[0].message.content)

def call_model_for_image2():
    print("Sending image to the LLM...")
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user", "content": [
                    {"type": "text", "text": "Qui di seguito trovi un estratto del testo dall'immagine. Puoi usare questo estratto per rispondere alle domande dell'utente."},
                    {"type": "text", "text": IMAGE_EXTRACTED_TEXT}
                ]
            },
            {
                "role": "user", "content": [
                    {"type": "text", "text": """A quanti gradi tedeschi corrisponde il livello "Dolce" della durezza dell'acqua?"""},
                    {"type": "image_url", "image_url": { "url": f"data:image/png;base64,{base64_image}" } }
                ]
            }
        ],
        temperature=0.1,
        model=MODEL
    )
    print("...complete.")

    print(response.choices[0].message.content)

def call_model_for_image3():
    print("Sending image to the LLM...")
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user", "content": [
                    {"type": "text", "text": "Qui di seguito trovi un estratto del testo dall'immagine. Puoi usare questo estratto per rispondere alle domande dell'utente."},
                    {"type": "text", "text": IMAGE_EXTRACTED_TEXT}
                ]
            },
            {
                "role": "user", "content": [
                    {"type": "text", "text": """Trascrivi parola per parola, il contenuto del capitolo 'REGOLAZIONE DEL DOSAGGIO DI BRILLANTANTE'.
                        Devi ricopiare *esattamente* le parole come sono scritte, non usare sinonimi o abbreviazioni, non tentare di interpretare il testo,
                        trascrivi *esattamente* quello che vedi."""},
                    {"type": "image_url", "image_url": { "url": f"data:image/png;base64,{base64_image}" } }
            ]
            }
        ],
        temperature=0.1,
        model=MODEL
    )

    print(response.choices[0].message.content)


print("Starting...")
call_model()
print()

print("Image Test 1...")
call_model_for_image1()
print()

print("Image Test 2...")
call_model_for_image2()
print()

print("Image Test 3...")
call_model_for_image3()
print()
print("Done.")