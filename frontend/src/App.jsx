import { useState } from 'react'
import {
  Flex,
  Button,
  Box,
  Input,
  InputGroup,
  InputRightElement,
  IconButton,
  Stack,
  Heading,
  useToast
} from '@chakra-ui/react'
import { LinkIcon } from '@chakra-ui/icons'

function App() {
  
  const [value, setValue] = useState("")
  const [loading, setLoading] = useState(false) // <--- Estado de carga
  const toast = useToast()

  const handlePaste = async () => {
    try {
      const ytRegex = /^(https?:\/\/)?(www\.)?(youtube\.com|youtu\.be)\/.+$/;

      const text = await navigator.clipboard.readText()
      console.log("Clipboard:", text)

      if(ytRegex.test(text))
        setValue(text)
      else
        alert("Ingresa una url valida")

    } catch (err) {
      console.error("Clipboard error:", err)
      alert("Clipboard access blocked by browser")
    }
  }

const handleDownload = async () => {
    if (!value) return;

    setLoading(true)
    try {
      const response = await fetch(`http://localhost:8000/download?url=${encodeURIComponent(value)}`);

      if (response.ok) {
        const blob = await response.blob();
        const downloadUrl = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = downloadUrl;
        a.download = "cancion.mp3";
        document.body.appendChild(a);
        a.click();
        a.remove();
        
        toast({ title: "¡Descarga iniciada!", status: "success" })
        setValue("")
      } else {
        toast({ title: "Error", description: "El backend rechazó la petición", status: "error" })
      }
    } catch (error) {
      console.error(error);
      toast({ title: "Error de conexión", status: "error" })
    }
    setLoading(false)
  }

  return (
    <>
      <Box
        position="relative"
        minH="100vh"
        bg="red.500"
      >
        <Flex 
          minH  =   "100vh"
          align =   "center" 
          justify = "center"
        >
          <Box
            bg="white"
            p={5}
            w="100%"
            maxW="500px"
            borderRadius="md"
            textAlign="center"
          >
            <Stack spacing={4}>
              <Heading as="h1">
                Red Downloader
              </Heading>

              <InputGroup size="md">
                <Input
                  type="text"
                  placeholder="Pega el link aquí"
                  pr="4.5rem"
                  value={value}
                  onChange={(e) => setValue(e.target.value)}
                  disabled={loading}
                />

                <InputRightElement width="4.5rem">
                  <IconButton
                    aria-label="Pegar link"
                    icon={<LinkIcon />}
                    h="1.75rem"
                    size="sm"
                    colorScheme="gray"
                    variant="ghost"
                    onClick={handlePaste}
                    isDisabled={loading}
                  />
                </InputRightElement>
              </InputGroup>

              <Button
                bg="red.600"
                color="white"
                size="lg"
                _hover={{ bg: 'red.700' }}
                onClick={handleDownload} 
                isLoading={loading}      
                loadingText="Convirtiendo..."                
              >
                Descargar MP3
              </Button>
            </Stack>
          </Box>
        </Flex>
      </Box>
    </>
  )
}

export default App
