# Enables deprecation warnings globally in the application.
Warning[:deprecated] = true

module WarningOverrides
  DEPRECATION_WARNINGS = [
    "Using the last argument as keyword parameters is deprecated",
    "Passing the keyword argument as the last hash parameter is deprecated",
    "Splitting the last argument into positional and keyword parameters is deprecated",
  ].freeze

  def warn(message)
    if DEPRECATION_WARNINGS.any? { |msg| message.include?(msg) }
      Kernel.warn("[RUBY-3-WARNING] #{message}") # Kernel.warn writes to $stderr
    end
  end
end

module Warning
  prepend WarningOverrides
end

# Kernel.warn from ruby
# $stderr: It is used to display error messages, warnings, and other diagnostic information.
# ** in this case $stderr catch by datadog
# Warning is a core Ruby module
# prepend is a Ruby method that inserts a module at the beginning of the method lookup chain.
# Datadog, the setup must be configured to capture and forward $stderr logs properly.