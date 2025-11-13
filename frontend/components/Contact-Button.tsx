import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"

export function ContactButton({className}: {className?: string}) {
  return (
    <div>
      <Button className={cn("variant-default", className)}>Contact Us</Button>
    </div>
  )
}
