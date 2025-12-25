import { useState } from 'react'
import {
  AbsoluteCenter,
  Button,
  Box,
  Input,
  InputGroup,
  InputRightElement,
  IconButton,
  Stack,
  Heading
} from '@chakra-ui/react'
import { LinkIcon } from '@chakra-ui/icons'

function App() {
  const [value, setValue] = useState("")

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

  return (
    <>
      <Box
        position="relative"
        minH="100vh"
        bg="red.500"
      >
        <AbsoluteCenter axis="both">
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
                  />
                </InputRightElement>
              </InputGroup>

              <Button
                bg="red.600"
                color="white"
              >
                Descargar
              </Button>
            </Stack>
          </Box>
        </AbsoluteCenter>
      </Box>
    </>
  )
}

export default App
