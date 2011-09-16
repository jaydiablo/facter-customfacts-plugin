# Custom facts
custom_facts_path = "/etc/facts/*"
Dir.glob(custom_facts_path).each do |fact_file|
   Facter.add(fact_file.split(File::SEPARATOR)[-1]) do
      setcode do
         begin
            File.new(fact_file, "r").gets.chomp
         rescue => err
         end
      end
   end
end
